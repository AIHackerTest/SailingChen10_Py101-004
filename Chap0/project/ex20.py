# coding=utf-8

# inports the argv function(?) from the sys library
from sys import argv

# sets up 'argv' to accept the script and 'test.txt' file as input
script, input_file = argv

# creates a function 'print_all(f)' which reads and prints the input
def print_all(f):
    print (f.read())

# creates a function 'rewind(f)' which sets the input files current position
# to 0 via the 'seek()' function (this is in bytes i.e the start of the file)
def rewind(f):
    f.seek(0) # 调回第一个字节

# creates a function that accepts an integer (in this case from 'current_line')
# denoting the line to read and then reads that line with the 'readline()'
# function.
# NOTE - readline() reads a single line up to the \n character but leaves the
# \n character at the end of the lien, so the automatically advances the file
# position by 1 line for every time the function is called and leaves a blanket
# newline in place. that why there's a line break in the output code.
# that's how this script is reading, printing and advancing each line in turn.
def print_a_line(line_count, f):
    print (line_count, f.readline()) # readline() 一次只读一行内容，遇到\n会自动停止

#sets 'current_file' to equal the file object 'input_file', which is defined
# in the arguments when running the script, in this case it's 'test.txt'
current_file = open(input_file) # 打开文件

# prints the whole file on a newline under the print statement
print ("First let's print the whole file:\n")

# calls the function 'print_all' using 'current_line' as the parameter
print_all(current_file) # 执行定义的 print_all 函数，将 txt 文件内容全部读取并打印

print ("Now let's rewind, kind of like a tape.")

rewind(current_file)

print ("Let's print three lines:")

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)
