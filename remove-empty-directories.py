import shutil
import os,sys
from fnmatch import fnmatch

from glob import glob
import string


tempsrc = 'aasda'
path = "D:\My Music\Un"

def removeEmptyFolders(path):
		if not os.path.isdir(path):
				return

# remove empty subfolders
		files = os.listdir(path)
		if len(files):
				for f in files:
						fullpath = os.path.join(path, f)
						if os.path.isdir(fullpath):
								removeEmptyFolders(fullpath)

# if folder empty, delete it
		files = os.listdir(path)
		if len(files) == 0:
				#print "Removing empty folder:", path
				
				os.rmdir(path)

removeEmptyFolders(path)

def print_fnmatches1(pattern,dir,files):
		for filename in files:
				global tempsrc 
				if tempsrc != dir:
						temp = dir
						#print dir
						filenames = glob(dir+'\\*.mp3')
						total = glob(dir+'\\*')
						totalf = glob(dir+'\\*.*')
						#print '\b',len(filenames)+len(total)-len(totalf)
						if len(filenames)+len(total)-len(totalf) == 0:
								#print 'aaa'
								try:
										shutil.rmtree(dir)
								except WindowsError:
										pass
						else:
								tempsrc = dir
				if fnmatch(filename, pattern):
						src1 = os.path.join(dir, filename)
						
						


os.path.walk(path,print_fnmatches1,'*.')