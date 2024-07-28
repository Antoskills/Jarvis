
import os
from playsound import playsound
import datetime

extracted_time = open('C:\\Users\\asus\\Desktop\\HOW TO MAKE JARVIS\\Data.txt')
time = extracted_time.read()
Time =str(time)

delete_time = open('C:\\Users\\asus\\Desktop\\HOW TO MAKE JARVIS\\Data.txt')
delete_time.truncate(0)
delete_time.close()

print(Time)





