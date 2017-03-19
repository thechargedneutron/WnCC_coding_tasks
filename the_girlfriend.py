"""
Q2. The Girlfriend. Brief outline of the logic is given in the Readme section
"""


import time
import os


"""
FUNCTION TO CONVERT TIMESTAMP INTO SECONDS
"""
def give_time(x):
	time_grab=x.split(" ")
	time_grab[0]=time_grab[0].replace(",",":")
	time_grab[2]=time_grab[2].replace(",",":")
	x=time_grab[0].split(":",4)
	y=time_grab[2].split(":",4)
	y[3]=y[3][0:3]
	time_start=float(x[0])*3600+float(x[1])*60+float(x[2])+float(x[3])*0.001
	time_end=float(y[0])*3600+float(y[1])*60+float(y[2])+float(y[3])*0.001
	return (time_start,time_end)


"""
OPENING THE LYRICS.SRT FILE
"""

with open("lyrics.srt","r") as myfile:
	data=myfile.readlines()

length=len(data)
info=[]                                                        #info IS THE LIST WHICH CONTAINS SET OF SUBTITLES i.e. [time_start,time_end,subtitles]
i=0                                                            #i IS THE ITERATOR TO TRACK THE LINES OF FILE
if data[0].find("0")!=-1:
	j=0
if data[0].find("1")!=-1:
	j=1                                                    #j IS THE ITERATOR TO TRACK THE SUBTITLE NUMBER
while i<length:
	q=[]
	if data[i]=='\xef\xbb\xbf'+str(j)+'\r\n' or data[i]==str(j)+'\r\n' or data[i]=='\xef\xbb\xbf'+str(j)+'\n' or data[i]==str(j)+'\n' or data[i]==str(j):
		p=give_time(data[i+1])                         #GET TIME FROM THE NEXT LINE OF THE SERIAL NUMBER LINE
		time_start=p[0]
		time_end=p[1]
		temp=i
		while any(c.isalpha() for c in data[i+2]) or any(c.isdigit() for c in data[i+2]):      #LOOP TO STORE ALL LINES OF A PARTICULAR TIMESTAMP IN A  temp LIST
			q.append(data[i+2])
			i=i+1
		j=j+1
		x=[time_start,time_end,q]
		info.append(x)
	i=i+1

x=[]                                                                                                         #x STORES TIME STAMPS CONVERTED INTO SECONDS
for i in range(0,len(info)):
	x.append(info[i][0])
	x.append(info[i][1])

"""
TILL NOW WE STORED THE CONTENTS OF THE GIVEN SRT FILE IN A LIST HAVING FIRST AND SECOND ELEMENT AS START AND END TIME RESPECTIVELY AND THIRD ENTRY AS THE THE SUBTITLES
"""

"""
NOW WE TAKE A LIST x AND PUT THE TIMESTAMPS IN IT AND THEN SORT IT.
AND THEN WE MAKE A LIST new WHICH CONTAINS ALL THE TIMESTAMPS IN INCREASING ORDER WITH SUBTITLES OF ALL THE OVERLAPPING TIMESTAMPS
"""
x.insert(0,0)                                                                                                #INSERT 0 AT THE BEGINNING OF THE TIME SAMPLES
x.sort()
new=[]                                                                                                      #new IS THE RECONSTRUCTED VERSION OF data HAVING ALL THE SUBTITLES IN THE SAME LIST
temp=[]
for i in range(0,len(x)-1):
	temp=[]
	for j in range(0,len(info)):
		if info[j][0]<= x[i] and info[j][1]>=x[i+1]:
			f=len(info[j][2])
			for foo in range(0,len(info[j][2])):
				temp.append(info[j][2][foo])
		if [x[i],x[i+1],temp] not in new:
			new.append([x[i],x[i+1],temp])


"""
DISPLAYING THE FINAL RESULT

"""

for foo in range(0,len(new)):
	os.system('clear')
	for goo in range(0,len(new[foo][2])):
		print new[foo][2][goo]
	#print new[foo][1]
	time.sleep(new[foo][1]-new[foo][0])
