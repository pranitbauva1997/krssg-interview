#!/usr/bin/python3
import time

title = input("Enter Title of the post : ")
content = input("Enter contents of the post : ")
filename = str(int(time.time()))

f = open("posts/" + filename + ".post", "w")
f.write("title:" + title + "\n" + "content:" + content + "\n" + "date:" + time.strftime("%d/%m/%Y") + "\n" + "time:" + time.strftime("%H:%M:%S") + "\n")
print("Thank You! Your post has been added. \n")
