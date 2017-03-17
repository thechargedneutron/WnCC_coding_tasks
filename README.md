# WnCC_coding_tasks
Hey There,
This repository contains the solution of the coding assignment for WnCC, IIT Bombay selection process.
My attempted question and my approach toward this problem is briefly described below:

Attempted Question: 2. The Girlfriend (including bonus problem)

Programing Language used: Python 2

Approach:
A while loop reads all the data of the given srt file into a list, having the three elements as start time, end time and content of the subtitles

A different list takes all the time samples(start time and end time) and sort them in ascending order.

A final list is made, which has all the consecutive time and all the possible subtitles that is to be displayed in that time frame.
This final list is displayed at the output window at assigned intervals using time.sleep() function.

NOTE: This code is able to display overlapping subtitles, i.e. I have solved the bonus problem also
