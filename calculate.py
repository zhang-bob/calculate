__author__ = 'zhangb3'

import sys
import os.path

MAX_NUM_PER_LINE=2000
MAX_LINE_NUM=50000

class Calculate:
    """this class is defined to calculate sum of numbers in a input file"""
    def __init__(self):
        pass

    def execute(self):
        file_name = self.get_from_argument()

        (number, sum) = self.calculate(file_name)

        self.print_result(number, sum)

    def print_result(self, number, sum):
        print "The number of float number in this file is %s" % number
        print "The sum of all float number is %s" % sum

    def calculate(self, testfile):
        number= 0
        sum = float(0)

        try:
            # return if size of file exceed maximum
            lines_num = self.get_line_number(testfile)
            if lines_num > MAX_LINE_NUM :
                raise Exception("The max line we support is %s, but current line is %s" % (MAX_LINE_NUM, lines_num))

            f = open(testfile,'r')
            for line in f:
                if len(line.split()) > MAX_NUM_PER_LINE:
                    raise Exception("The max data in one line is %s, but current value is %s" % (MAX_NUM_PER_LINE,
                    len(line.split())))
                for data in line.split():
                    # skip invalid string which can't be converted to float type
                    try:
                        float_number = float(data)
                    except:
                        continue

                    number += 1
                    sum = sum + float_number
        except(Exception), e:
            print e
            print "Encounter unexpected error, please try again later"
        finally:
            f.close()
        return (number, sum)

    def get_line_number(self, testfile):
        try:
            f = open(testfile, 'r')
            lines_num = len(f.readlines())
        except(Exception), e:
            raise Exception("fail to get length of file %s" % testfile)
        finally:
            f.close()

        return lines_num

    def usage(self):
        print "%s <input file>" % sys.argv[0]
        sys.exit(0)

    def get_from_argument(self):
        if len(sys.argv) == 1 or len(sys.argv) > 3:
            self.usage()

        file_name = sys.argv[1]

        if not os.path.isfile(file_name):
            print "the input you give %s is not a file, please check again" % file_name
            sys.exit(1)

        return file_name

if __name__ == '__main__':
    calculator = Calculate()
    calculator.execute()
