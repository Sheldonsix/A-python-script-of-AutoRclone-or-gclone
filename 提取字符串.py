import re
import sys
import os,glob

# 定义目录：目录下有多个文件需要处理
path = 'D:\\下载\\Telegram Desktop\\accounts\\accounts'
# 定义输出文件
fout = open("res.txt", 'w')

os.chdir(path)

fout.write("用户名和邮箱（便于查询）\n")
for filename in os.listdir() :
    fs = open(filename, 'r+')
    fout.write("文件名：" + filename + '\n')
    for line in fs.readlines():
        mylist_1 = line.split(":")
        if mylist_1[0] == "  \"client_email\"" :
            mylist_2 = mylist_1[1].split("\"")
            fout.write(mylist_2[1] + '\n')


fout.write("\n\n")
fout.write("邮箱（便于添加到 Google group）\n")
for filename in os.listdir() :
    fs = open(filename, 'r+')
    for line in fs.readlines():
        mylist_1 = line.split(":")
        if mylist_1[0] == "  \"client_email\"" :
            mylist_2 = mylist_1[1].split("\"")
            fout.write(mylist_2[1] + '\n')
fout.write('\n')
fout.close()
'''
fh = open('D:\\下载\\Telegram Desktop\\accounts\\accounts\\00bdf07c476792985eeb9bf69ef5f154669e845f.json')
for line in fh.readlines() :
    if line != "}" :
        mylist = line.split(":")
        if mylist[0] == "  \"client_email\"" :
            #print(mylist[1])
            mylist_2 = mylist[1].split("\"")
            print(mylist_2[1])
'''

        
        