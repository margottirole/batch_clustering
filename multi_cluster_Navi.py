#!/usr/bin/env python3

import sys
import os
import multiprocessing
import subprocess
import time
import shutil

# change to your data path
directory_path = os.path.join('E:/','CheetahData','Navi','2018-10-07_10-41-04')

# change to your parameters file folder containing the .prm, .prb, ncs2dat.py and this script
parameter_path= os.path.join('E:/', 'Parameter_Files')

#change to your klusta folder
 # klusta_path = os.path.join('C:/', 'klusta')
 # os.system('activate klusta')

os.chdir(directory_path)

# change according to your tetrode configuration
tetrode_list=[1, 2, 17, 18,
				3, 4, 19, 20,
				5, 6, 21, 22,
				7, 8, 23, 24,
				9, 10, 25, 26,
				11, 12, 27, 28,
				13, 14, 29, 30,
				15, 16, 31, 32,
				33, 34, 49 ,50,
				35, 36 ,51 ,52,
				37, 38, 53, 54,
				39 ,40, 55 ,56,
				41, 42, 57, 58,
				43, 44 ,59 ,60,
				45 ,46 ,61, 62,
				47,48,63,64]

def createFolder(directory):
		try:
			os.mkdir(directory)
		except OSError:
			print ("Creation of the directory %s failed" % directory)
		else:
			print ("Successfully created the directory %s " % directory)

def runklust(tetrode,folder_path,i):
	os.chdir(folder_path)
	prm_file= os.path.join(tetrode + '.prm')
	print('klusta ' + prm_file + ' --overwrite')
	subprocess.call('klusta ' + prm_file + ' --overwrite', creationflags = subprocess.CREATE_NEW_CONSOLE)


if __name__ == '__main__':
		jobs=[]
		for i in range(1,17):
			tetrode= 'tetrode' + "_%d" % (i)
			dat_file= os.path.join(directory_path, 'tetrode' + "_%d.dat" % (i))
			prm_file= os.path.join(parameter_path, 'tetrode' + "_%d.prm" % (i))
			prb_file= os.path.join(parameter_path, '1tet.prb')
			folder_path= os.path.join(directory_path, 'tetrode' + "_%d" % (i))
							
			if not os.path.exists(dat_file):
				command_line = ["CSC%d.ncs" %n for n in tetrode_list[4*i-4:4*i]]
				command_line= ' '.join(command_line)
				ncs2dat_path= os.path.join(parameter_path, 'ncs2dat.py')
				os.system('python ' + ncs2dat_path + ' ' + command_line + ' ' + dat_file) 
				
			createFolder(folder_path)
			shutil.copy(dat_file, folder_path)
			shutil.copy(prm_file, folder_path)
			shutil.copy(prb_file, folder_path)
			
			p = multiprocessing.Process(target=runklust, args=(tetrode,folder_path,i,))
			jobs.append(p)
			p.start()
			
		for j in jobs:
			j.join()
			print('%s.exitcode = %s' % (j.name, j.exitcode))
		
		for i in range(1,17):
			folder_path= os.path.join(directory_path, 'tetrode' + "_%d" % (i))
			tetrode= 'tetrode' + "_%d" % (i)
			kwik_file= os.path.join(folder_path, tetrode + '.kwik')
			kwx_file= os.path.join(folder_path, tetrode + '.kwx')
			shutil.move(kwik_file, directory_path)
			shutil.move(kwx_file, directory_path)
			shutil.rmtree(folder_path)
			os.chdir(directory_path)

				
