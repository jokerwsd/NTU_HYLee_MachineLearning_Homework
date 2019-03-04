#input hw0_data.at and column number
#output column in sorted order

import sys
import csv
if len(sys.argv) != 3:
	print("Usage: judy_q1.py [input.data] [column number]")

input_file_name = sys.argv[1]
col = int(sys.argv[2])
with open(input_file_name) as input_file:
	reader = csv.reader(input_file, delimiter=" ")
	reader_col = zip(*reader)


line = list(reader_col[col])
line.sort()

with open('result/ans1.txt', 'w') as f:
	f.write(','.join(line))