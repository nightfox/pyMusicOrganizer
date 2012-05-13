from fnmatch import fnmatch
import os, os.path
from eyeD3 import *

path = "/Users/anirvan/n!ghtf0x's Stuff/Music/Unorganized/Hindi/"
def cleanTag(tagname):
	tagname = string.replace(tagname,' - www.Songs.PK','')
	tagname = string.replace(tagname,'[Songs.PK]','')
	tagname = string.replace(tagname,'www.Songs.PK','')
	tagname = string.replace(tagname,'www.songs.pk','')
	tagname = string.replace(tagname,' - ','')
	tagname = string.capitalize(tagname)
	return tagname	 


def songsCorrect(location):
		tag = eyeD3.Tag()
		val = tag.link(location)
		if val == 0:
				tag.header.setVersion(eyeD3.ID3_V2_3)
				tag.setArtist('Unknown')
				tag.setTitle('Unknown')
				tag.setAlbum('Unknown')
				try:
						tag.update()
				except TypeError, eyeD3.tag.TagException:
						a = 11
		else:
				title = tag.getTitle().encode('ascii','ignore')
				title = cleanTag(title) 
				tag.setTitle(title)
				artist = tag.getArtist().encode('ascii','ignore')
				artist = cleanTag(artist)
				tag.setArtist(artist)
				tag.removeLyrics()
				try:
						tag.update()
				except TypeError:
						a = 11
				except eyeD3.tag.TagException:
						b = 1


def print_fnmatches(pattern, dir, files):
		for filename in files:
				if fnmatch(filename, pattern):
						bcd = os.path.join(dir, filename)
						print bcd
						try :
								songsCorrect(bcd)
						except ValueError:
								a = 2
os.path.walk(path, print_fnmatches, '*.mp3')
