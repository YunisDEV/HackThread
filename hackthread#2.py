#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = []

    for i in arr:
        result.insert(0,i)

    print(' '.join(map(str,result)))
