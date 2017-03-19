# WnCC_coding_tasks
Hey There,
This repository contains the solution of the coding assignment for WnCC, IIT Bombay selection process.
My attempted question and my approach toward this problem is briefly described below:

Attempted Question: 2. (COMPLETED) The Girlfriend (including bonus problem)

Programing Language used: Python 2

Approach:
A while loop reads all the data of the given srt file into a list, having the three elements as start time, end time and content of the subtitles

A different list takes all the time samples(start time and end time) and sort them in ascending order.

A final list is made, which has all the consecutive time and all the possible subtitles that is to be displayed in that time frame.
This final list is displayed at the output window at assigned intervals using time.sleep() function.


NOTE: This code is able to display overlapping subtitles, i.e. I have solved the bonus problem also
      A sample .srt file is also attached with it. The subtitles is of 'Rap God' by Eminem (couldn't find a faster song).
      Although I couldn't find an overlapping subtiles, this works fine with them. (tested by modifying the time stamps :P )
EDIT: Due to a slight mistake in the .srt file that I chose, the time stamp was beginning from 0. According to Wikipedia, it should begin with 1. Owning to this confusion, the file has been changed and it accpets both the starting stamp.


Attempted Question: 1. (COMPLETED) The R-Rated Artist

Programming Language used: Python 2

Approach:
Due to the high traffic of azlyrics.com, and also because the website refuses if the number of queries is more than a certain limit, the program, initialy made for azlyrics.com has been modified to work on lyrics.wikia.com.
The input.txt is read and the corresponding artist's song list is obtained by scraping azlyrics.com
The songs are then individually scrpaed from lyrics.wikia.com page and then the target worded is counted without considering the case sensitivity.

Since it requires the programe to scrape data from around 2000 webpages, the time of execution varies according to the speed of internet. On a slow Jio mobile hotspot, the program completed succesfuly in around 15-20 minutes. The time will be much less if VPN is used in IITB network, since azlyrics is blocked by the institute.

NOTE: This code was built after getting to know we are allowed to use other webpages also, thus reducing the time that we can code to around 20 hours.
