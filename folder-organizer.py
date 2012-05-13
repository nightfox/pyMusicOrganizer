import shutil
import os,sys
from fnmatch import fnmatch
from eyeD3 import *
from glob import glob
import string

if len(sys.argv)< 2:
		sys.exit('Usage: %s -h/-e' % sys.argv[0])
tempsrc = 'random name'
if sys.argv[1] == '-e':
		path = "/Users/anirvan/n!ghtf0x's Stuff/Music/English songs"
		source = "/Users/anirvan/n!ghtf0x's Stuff/Music/Unorganized/English/"
		print "Moving files from English Temp to iTunes Library"
elif sys.argv[1] == '-h':
		path = "/Users/anirvan/n!ghtf0x's Stuff/Music/Hindi songs"
		source = "/Users/anirvan/n!ghtf0x's Stuff/Music/Unorganized/Hindi/"
		print 'Moving files from Hindi Temp to iTunes Library'
else:
		sys.exit('Argument can only be \'-e\' or \'-h\'')


def directoryCreator(src):
		tag = eyeD3.Tag()
		val = tag.link(src)
		if val == 1:
				artist = tag.getArtist().encode('ascii','ignore')
				artist = string.replace(artist,'/',' , ')
				album = tag.getAlbum().encode('ascii','ignore')
				artist = string.capwords(artist)
				album = string.capwords(album)
				album = string.replace(album,':','')
				if artist != '' and album != '':
						dir,name = os.path.split(src)
						newDir = string.join((path,artist,album),'/')
						if os.path.exists(newDir) == False:
								try:
										os.makedirs(newDir)
								except WindowsError:
										print 'Could not create the directory '+ newDir
						dst = os.path.join(newDir,name)
						try:
								shutil.move(src,dst)
								print 'File moved --> '+ dst
						except IOError:
								print 'File Could not be moved. Check folder permissions.'
				else:
						dir,name = os.path.split(src)
						newDir = string.join((path,'Info Missing'),'/')
						if os.path.exists(newDir) == False:
								try:
										os.makedirs(newDir)
								except WindowsError:
										print 'Could not create the directory '+ newDir
						dst = os.path.join(newDir,name)
						try:
								shutil.move(src,dst)
								print 'File moved --> '+ dst
						except IOError:
								print 'File Could not be moved. Check folder permissions.'
						
		else:
				dir,name = os.path.split(src)
				newDir = string.join((path,'Incorrect Tag'),'/')
				if os.path.exists(newDir) == False:
						try:
								os.makedirs(newDir)
						except WindowsError:
								print 'Could not create the directory '+ newDir
				dst = os.path.join(newDir,name)
				try:
						shutil.move(src,dst)
						print 'File moved --> '+ dst
				except IOError:
						print 'File Could not be moved. Check folder permissions.'

def print_fnmatches(pattern,dir,files):
		for filename in files:
				if fnmatch(filename, pattern):
						src = os.path.join(dir, filename)
						try:
								directoryCreator(src)
						except ValueError:
								pass

os.path.walk(source,print_fnmatches,'*.mp3')



# Uncomment Code for source folder Cleanup
# Contains bugs below

"""def removeEmptyFolders(path):
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
				if path == source:
						pass
				else:
						print "Removing empty folder:", path
						os.rmdir(path)

#removeEmptyFolders(source)

def print_fnmatches1(pattern,dir,files):
		for filename in files:
				global tempsrc 
				if tempsrc != dir:
						temp = dir
						print dir
						filenames = glob(dir+'\\*.mp3')
						total = glob(dir+'\\*')
						totalf = glob(dir+'\\*.*')
						print '\b',len(filenames)+len(total)-len(totalf)
						if len(filenames)+len(total)-len(totalf) == 0:
								print 'aaa'
								try:
										shutil.rmtree(dir)
								except WindowsError:
										pass
						else:
								tempsrc = dir
				if fnmatch(filename, pattern):
						src1 = os.path.join(dir, filename)
						
						


os.path.walk(source,print_fnmatches1,'*.mp3')"""

 
