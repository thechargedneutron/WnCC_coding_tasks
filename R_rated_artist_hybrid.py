import urllib2
from bs4 import BeautifulSoup
import unicodedata



#### MODULE1:  TO OPEN TEXT FILE AND STORE THE NAME OF ARTIST IN REQUIRED FORM

with open("input.txt","r") as myfile:
	data=myfile.readlines()

#print data
input_artist=data[:]
#print data[2].lower()
artist=[]
alias=[]                                                                    #ALIAS STORES THE ALTERNATE POSSIBLE URL TITLE, eg. west IN CASE OF Kayne West
for i in range(0,len(data)):
	input_artist[i]=input_artist[i].replace(" ","_")                    #MAKING IT LOOK LIKE ARTIST NAME IN AZLYRICS WEBSITE
	input_artist[i]=input_artist[i].rstrip()
	#data[i]=data[i].replace(" ","")
	data[i]=data[i].lower()
	#print data[i]
	#print "Hii"
	data[i]=data[i].rstrip()
	temp=data[i].split(" ")
	data[i]=data[i].replace(" ","")
	#print temp
	alias.append(temp)                                                 #MAKING THE ALIAS LIST
	j=0
while(data[j] != ''):
	artist.append(data[j])
	#alias.append(temp)
	j=j+1
target_word=data[j+1]
target_word=target_word.lower()                                            #THE TARGET WORD AND WORDS OF LYRICS ARE CONVERTED TO LOWER CASE TO REMOVE CASE SENSITIVITY
#print artist
#print alias
#print target_word
#print input_artist



### MODULE2: TO OPEN AZLYRICS ARTIST PAGE FOR EACH ARTIST AND GET THE LIST OF SONGS AND THEN USE THEM IN LYRICS.WIKI PAGE FOR THE SONG

count_of_target_word=[]
for foo in range(0,len(artist)):
	counting=0
	try:
		soup=BeautifulSoup(urllib2.urlopen('http://www.azlyrics.com/'+artist[foo][0]+'/'+artist[foo]+'.html').read(),"lxml")         #TO OPEN SONGS PAGE, IF IT FAILS, TRY OPENING IT USING ALIAS
		data=soup.get_text()
		x=200
	except urllib2.HTTPError,e:
		print e.code
		x=404
	except urllib2.URLError,e:
		print e.args
		x=404
	if x==404 :
		k=0
		while True:
			try:
				soup=BeautifulSoup(urllib2.urlopen('http://www.azlyrics.com/'+alias[foo][k][0]+'/'+alias[foo][k]+'.html').read(),"lxml")      #TRYING USING ALIAS
				data=soup.get_text()
				y=200
			except urllib2.HTTPError,e:
				print e.code
				y=404
			except urllib2.URLError,e:
				print e.args
				y=404
			if y==200:
				#artist[foo]=alias[foo][k]   #kch bhi?
				break

			if k>len(alias[foo]):
				print "Sorry, artist not found"			
			else:
				k=k+1
			
	#for j in range(0,len(data)):
		#print j,data[j]
	######### MODULE 3: TO CONVERT THE AVAILABLE TEXTS IN THE ARTIST PAGE AND EXTRACT THE NAME OF SONGS
	lines=[]
	spelling=''
	for j in range(0,len(data)):
		if data[j]=="\n":
			lines.append(spelling)
			spelling=''
		else:
			spelling=spelling+data[j]
	#print lines
	for i in range(0,len(lines)):
		#print i, lines[i]," \n"
		#print type(data[i])
		k=lines[i].find("sort by song")                        #THIS OCCURS BEFORE EVERY SONG IN AZLYRICS
		if k != -1:
			temp=i
			break
	for x in range(temp,len(data)):
		l=lines[x].find("<!--")                                #THIS OCCURS AT THE END OF EVERY SONG IN AZLYRICS
		if l != -1 :
			temp2=x
			break
	#print temp
	#print temp2
	list_of_songs= lines[temp+3:temp2]
	############ MODULE 4: TO CONVERT LIST OF SONGS INTO THE URL FORMAT OF THE lyrics.wikia PAGE	
	#print list_of_songs
	song_url=[]
	for i in range(0,len(list_of_songs)):
		#list_of_songs[i]=remove_u(list_of_songs[i])
		#list_of_songs[i]=list_of_songs[i].lower()
		list_of_songs[i]=list_of_songs[i].replace(" ","_")
		list_of_songs[i]=list_of_songs[i].replace("'","%27")
		#list_of_songs[i]=list_of_songs[i].replace("'","")
		#list_of_songs[i]=list_of_songs[i].replace("(","")
		#list_of_songs[i]=list_of_songs[i].replace(")","")
		list_of_songs[i]=list_of_songs[i].replace("&","%26")
		list_of_songs[i]=list_of_songs[i].replace("?","")
		list_of_songs[i]=list_of_songs[i].replace("\n","")
		#list_of_songs[i]=list_of_songs[i].replace(".","")
		list_of_songs[i]=list_of_songs[i].replace("/","")
		list_of_songs[i]=list_of_songs[i].replace(",","")
		#list_of_songs[i]=list_of_songs[i].replace("_","")  #pagal ho kya??
		list_of_songs[i]=list_of_songs[i].replace("-","")
		list_of_songs[i]=list_of_songs[i].replace("-","")
		list_of_songs[i]=unicodedata.normalize('NFKD', list_of_songs[i]).encode('ascii','ignore')
		list_of_songs[i]=list_of_songs[i].replace(u"\u2018", "")
		list_of_songs[i]=list_of_songs[i].replace(u"\u2019", "")
		list_of_songs[i]=list_of_songs[i].split("(featuring")[0]              #http://lyrics.wikia.com/wiki/Eminem:%2797_Bonnie_%26_Clyde
		list_of_songs[i]=list_of_songs[i].split("[")[0]
		song_url.append("http://lyrics.wikia.com/wiki/"+input_artist[foo]+":"+list_of_songs[i])                          #MAKING THE URL OUT OF SONG NAME
		#song_url.append("http://www.azlyrics.com/lyrics/"+artist[foo]+"/"+list_of_songs[i]+".html")
		#print list_of_songs[i]
		#print song_url[i]
		print "Collecting data from ",song_url[i]
		try:                                                                                                           #COLLECT DATA FROM lyrics.wikia WEBSITE
			soup=BeautifulSoup(urllib2.urlopen(song_url[i]).read(),"lxml")
			data2=soup.get_text()
			words_of_lyrics=[]
			spelling=''                                                        #SINCE SINGLE CHARACTER APPEARS AS AN ELEMENT, WE MAKE CLUSTER TO FORM WORDS
			for d in range(0,len(data2)):
				#print d,data2[d]
				if data2[d].isalpha() and data2[d+1].isalpha():
					spelling=spelling+data2[d]
				if data2[d].isalpha() and data2[d+1].isalpha()==False:
					spelling=spelling+data2[d]
					words_of_lyrics.append(spelling)
					spelling=''
			for x in range(0,len(words_of_lyrics)):                            #IF WORD MATCHES THE target_word, INCREMENT THE counting VARIABLE
				words_of_lyrics[x]=words_of_lyrics[x].lower()
				l=words_of_lyrics[x].find(target_word)
				if l != -1:
					counting=counting+1
			print "Total count till now= ",counting
		except urllib2.HTTPError,e:
			print e.code
		except urllib2.URLError,e:
			print e.args

	count_of_target_word.append(counting)
	#print song_url

### MODULE 5: TO SAVE THE ORDER OF ARTIST USING target_word IN THEIR SONG AND DISPLAY IN TERMINAL

print count_of_target_word
final_data=[]
for t in range(0,len(count_of_target_word)):
	input_artist[t]=input_artist[t].replace("_"," ")
	final_data.append([count_of_target_word[t],input_artist[t]])
print "\n","\n","\n"
print "The decreasing order of the occurence of the word ",target_word," is saved in Output.txt ","\n"
final_data.sort(reverse=True)
#for t in range(0,len(count_of_target_word)):
#	print final_data[t][1]


text_file = open("Output.txt", "w")
for u in range(0,len(count_of_target_word)):
	text_file.write(final_data[u][1])

text_file.close()
