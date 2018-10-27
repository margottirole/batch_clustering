#!/usr/bin/env python3

import sys
import os

directory_path = os.getcwd()

os.chdir(directory_path)
os.system('activate klusta')


for i in range(1,64,4):
	output_filename=  os.path.join(directory_path, 'tetrode' + "_%d.dat" % ((1/4)*(i+3)))
	if os.path.exists(output_filename) != 1:
		command_line = 'CSC%d.ncs CSC%d.ncs CSC%d.ncs CSC%d.ncs ' % (i, i+1, i+2, i+3)
		os.system('python ../ncs2dat.py ' + command_line + output_filename) 
	output_filename2=  os.path.join(directory_path, 'tetrode' + "_%d.prm" % ((1/4)*(i+3)))
	os.system('klusta ' + output_filename2 + ' --overwrite')
print('Done')	
