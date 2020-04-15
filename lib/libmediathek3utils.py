# -*- coding: utf-8 -*-
import xbmc
import xbmcplugin
import xbmcaddon
import xbmcvfs
import re
import sys
import gzip

def log(msg):
	xbmc.log(msg)

def getTranslation(id,addonid='script.module.libmediathek3'):
	return xbmcaddon.Addon(id=addonid).getLocalizedString(id)
	
		
		
		
		
		

def clearString(s):
	s = s.replace("&lt;", "<").replace("&gt;", ">").replace("&amp;", "&").replace("&#034;", "\"").replace("&#039;", "'").replace("&quot;", "\"").replace("&szlig;", "ß").replace("&ndash;", "-")
	s = s.replace("&Auml;", "Ä").replace("&Uuml;", "Ü").replace("&Ouml;", "Ö").replace("&auml;", "ä").replace("&uuml;", "ü").replace("&ouml;", "ö").replace("&eacute;", "é").replace("&egrave;", "è")
	s = s.replace("&#x00c4;","Ä").replace("&#x00e4;","ä").replace("&#x00d6;","Ö").replace("&#x00f6;","ö").replace("&#x00dc;","Ü").replace("&#x00fc;","ü").replace("&#x00df;","ß")
	#ISO-8859-1?!?!?! oh how i hate the friggin encoding
	s = s.replace("&apos;","'")
	s = s.replace("&#43;","\"")
	s = s.strip()
	return s
	
def pathUserdata(path):
	special = xbmcaddon.Addon().getAddonInfo('profile')+path
	special = special.replace('//','/').replace('special:/','special://')
	return special
	
def pathAddon(path):
	special = xbmc.validatePath(xbmcaddon.Addon().getAddonInfo('path').replace('\\','/')+path.replace('\\','/'))
	special = special.replace('//','/').replace('special:/','special://')
	return special
	
def f_open(path):
	try:
		f = xbmcvfs.File(path)
		result = f.read()
	except: pass
	finally:
		f.close()
	return result

def f_write(path,data):
	try:
		#f_mkdir(path)
		f = xbmcvfs.File(path, 'w')
		result = f.write(data)
	except: pass
	finally:
		f.close()
	return True

def f_remove(path):
	return xbmcvfs.delete(path)
	
def f_exists(path):
	exists = xbmcvfs.exists(path)
	if exists == 0:
		return False
	elif exists == False:
		return False
	else:
		return True
	
def f_mkdir(path):
	return xbmcvfs.mkdir(path)
	
def searchWorkaroundWrite(searchword):
	f_write(pathUserdata('/search.lock'),searchword)
def searchWorkaroundRead():
	return f_open(pathUserdata('/search.lock'))
def searchWorkaroundExists():
	return f_exists(pathUserdata('/search.lock'))
def searchWorkaroundRemove():
	log('###Krypton workaround: removing lock...')
	f_remove(pathUserdata('/search.lock'))

def setSetting(k,v):
	return xbmcplugin.setSetting(int(sys.argv[1]), k, v)
	
def getSetting(k):
	return xbmcplugin.getSetting(int(sys.argv[1]), id=k)
	