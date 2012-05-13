from eyeD3 import *
import string
import os, sys
from fnmatch import fnmatch

if len(sys.argv)< 2:
		sys.exit('Usage: %s -h/-e' % sys.argv[0])
tempsrc = 'aasda'
if sys.argv[1] == '-e':
		path = "/Users/anirvan/n!ghtf0x's Stuff/Music/Unorganized/English/"
		print 'Renaming Songs in Temp English Folder'
elif sys.argv[1] == '-h':
		path = "/Users/anirvan/n!ghtf0x's Stuff/Music/Unorganized/Hindi/"
		print 'Renaming Songs in Temp Hindi Folder'
else:
		sys.exit('Argument can only be \'-e\' or \'-h\'')


def renamingFunc(file):
		eTag = eyeD3.Tag()
		val = eTag.link(file)
		if val == 1:
				if eTag.getArtist().encode('ascii','ignore') != 'Unknown' and eTag.getTitle().encode('ascii','ignore') != 'Unknown':
						filepath,filename = os.path.split(file)
						
						tempArtist = string.capwords(eTag.getArtist().encode('ascii','ignore'))
						tempTitle = string.capwords(eTag.getTitle().encode('ascii','ignore'))
						eTag.setArtist(tempArtist)
						eTag.setTitle(tempTitle)
						eTag.update()
						newFileName = tempArtist + ' - ' + tempTitle+'.mp3'
						newFileName = string.replace(newFileName,'/','')
						newFile = os.path.join(filepath,newFileName)
						
						try:
								os.rename(file,newFile)
								print filename + ' ==> ' + newFileName
						except WindowsError:
								print file + ' could not be renamed !'
		else:
				print 'Check the ID3 tags for ' + file
								
def print_fnmatches(pattern, dir, files):
		for filename in files:
				if fnmatch(filename, pattern):
						name = os.path.join(dir, filename)
						print name
						try:
								renamingFunc(name)
								
						except ValueError:
								print 'Internal Error with file !'
						
os.path.walk(path, print_fnmatches, '*.mp3')