import math
import os
import random
import re
import sys

def solve(s):
    s = ' '.join(word.capitalize() for word in s.split(" ")) #dont use split() for mantaining multiple spaces
    return s

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
