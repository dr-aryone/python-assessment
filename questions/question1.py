# -*- coding: UTF-8 -*-
"""
Question 1

# FizzBuzz

Write a program which prints the numbers from 1 to 107, each on a
new line. But for multiples of three print “Fizz” instead of the
number 3 and for the multiples of five print “Buzz” . For numbers
which are multiples of both three and five print “FizzBuzz. Read
in the input number from STDIN.

# Sample Input #00:
15

# Sample Output #00 :
1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz
"""

def main(input):
    # my code here
    for number in range(1,input+1):
        buzz = "Buzz" if not number % 3 else ""
        fizz = "Fizz" if not number % 5 else ""
        result =  fizz+buzz if buzz or fizz else number
        print result


if __name__ == "__main__":
    number = int(raw_input())
    main(number)