__author__ = 'zhangb3'

import sys
import random
import string

num_per_line=0
line_num=0
output_file = ""

def main():
    check_argv()

    data = generate_file()

    write_file(data)

def write_file(message):
    global output_file

    f = open(output_file, 'w')
    f.write(message)
    f.close()

def generate_file():
    line=0
    temp = ""
    global num_per_line
    global line_num

    while line < line_num:
        line += 1
        num=0
        while num < num_per_line:
            num += 1
            random_number = random.uniform(-10000, 10000)
            temp = temp + " " + str(random_number)
        temp = temp + "\n"

    return temp


def usage():
    print "%s <number of float per line> <the number of line> <output file>" % sys.argv[0]
    sys.exit(0)

def check_argv():
    global num_per_line
    global line_num
    global output_file

    if len(sys.argv) == 1 or sys.argv[1] == "-h":
        usage()

    if len(sys.argv) != 4:
        usage()

    try:
        num_per_line = int(sys.argv[1])
        line_num = int(sys.argv[2])
        output_file = sys.argv[3]
        print "line number is %d, number per line is %d" % (line_num, num_per_line)
    except:
        print "can't convert arguments, integer is expected"
        usage()
        sys.exit(1)

if __name__ == '__main__':
    main()



