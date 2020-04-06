import re
import sys
import os,glob

# 定义目录：目录下有多个文件需要处理，为 accounts 目录的路径，例如： path = 'D://AutoRclone//accounts'
path = 'path//to//your//accounts'
# 定义输出文件，路径可自定义，例如 fout = open("D://AutoRclone//accounts//res.txt", 'w')
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


        
        
