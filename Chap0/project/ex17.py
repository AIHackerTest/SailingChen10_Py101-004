# coding=utf-8
# import argv
# input exists

from sys import argv
from os.path import exists

script, from_file, to_file = argv

print ("Copying from %s to %s" % (from_file, to_file))

# we could do these two on one line too, how?
# 打开文件，只读文件
input = open(from_file)
indata = input.read()

# len() 字节长度
print ("The input file is %d bytes long" % len(indata))
# exists，存在与否，True or False
print ("Does the output file exist? %r" % exists(to_file))
print ("Ready, hit RETURN to continue, CTRL-C to abort.")

input() # input() 输入设置, 但运行时出错，TypeError: '_io.TextIOWrapper' object is not callable

# 'w' 以 write 模式打开文件
output = open(to_file, 'w')
# 在 output 文件中 write indata
output.write(indata)

print ("Alright, all done.")

output.close()
input.close()
