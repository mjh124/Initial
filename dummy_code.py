#!/usr/bin/python

# Script to sum up all of the numbers in a column

import sys
import math

if len(sys.argv) != 5:
        print "Usage: column_sum.py filename column-number total-summed-lines useless-lines"
        exit(0)

fn_name = sys.argv[1]
col = int(sys.argv[2])
tot = int(sys.argv[3])
skip = int(sys.argv[4])

fname = open(fn_name, 'r')
lines = fname.readlines()[skip:]
arr = []
for line in lines:
        tokens = line.split()[col]
        arr.append(float(tokens))

fname.close()
#print arr

add = math.fsum(arr)

print "Sum of column " + str(col) + " =", add
