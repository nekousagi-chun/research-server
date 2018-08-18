import os
import subprocess
import csv
import shlex


x = 1000
y = 200

file_list = ['cat']

for i in range(9):
	for j in range(9):
		file_list.append('{}_{}/output.csv'.format(y,x))
		y += 100
	x += 500
	y = 200

subprocess.call(shlex.split(' '.join(file_list)))
