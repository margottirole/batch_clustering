#!/usr/bin/env python3

import sys
import os

directory_path = os.getcwd()

klusta_path = os.path.join('C:/', 'klusta')
os.chdir(klusta_path)
os.system('activate klusta')
os.chdir(directory_path)


#cd C:/klusta
#activate klusta
#cd directory_path

#sys.path.insert(0, os.pardir)
#print(os.pardir)
#import ncs2dat


for i in range(1,64,4):
	output_filename=  os.path.join(directory_path, 'tetrode' + "_%d.dat" % ((1/4)*(i+3)))
	if os.path.exists(output_filename) != 1:
		command_line = 'CSC%d.ncs CSC%d.ncs CSC%d.ncs CSC%d.ncs ' % (i, i+1, i+2, i+3)
		os.system('python ../ncs2dat.py ' + command_line + output_filename) 
	output_filename2=  os.path.join(directory_path, 'tetrode' + "_%d.prm" % ((1/4)*(i+3)))
	os.system('klusta ' + output_filename2 + ' --overwrite')
print('Done')	