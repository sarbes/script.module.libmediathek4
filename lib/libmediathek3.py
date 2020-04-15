# -*- coding: utf-8 -*-

import xbmc
import xbmcgui
import xbmcplugin
import xbmcaddon
import sys

from libmediathek3utils import *
from libmediathek3listing import *
from libmediathek3ttml2srt import *
from libmediathek3premadedirs import *
from libmediathek3dialogs import *
	
class libmediathek:
	def addEntries(self,data):
		l = []
		for item in data['items']:
			if 'overridepath' in item:
				u = item['overridepath']
			else:
				u = self._buildUri(item['args'])

			liz = xbmcgui.ListItem(item['iLabels']['title'])
			liz.setInfo(type=data['addonType'],infoLabels=item['iLabels'])
			#liz.addStreamInfo('subtitle', {'language': 'deu'})
			#art
			
			if item.get('type',None) == 'video' or item.get('type',None) == 'live' or item.get('type',None) == 'date' or item.get('type',None) == 'clip' or item.get('type',None) == 'episode' or item.get('type',None) == 'audio' or item.get('type',None) == 'sport':
				#xbmcplugin.setContent( handle=int( sys.argv[ 1 ] ), content="episodes" )
				liz.setProperty('IsPlayable', 'true')
				lists.append([u,liz,False])
			else:
				lists.append([u,liz,True])

		if 'pagination' in data:
			u = self._buildUri(data['pagination']['args'])
			liz = xbmcgui.ListItem(translation(31040))
			liz.setInfo(type=data['addonType'])
			lists.append([u,liz,True])
		
		xbmcplugin.endOfDirectory(int(sys.argv[1]),cacheToDisc=True)	
		
	def _buildUri(d):
		u = d.get('pluginpath',sys.argv[0])+'?'
		i = 0
		for key in d.keys():
			if i > 0:
				u += '&'
			try:
				u += key + '=' + urllib.quote_plus(d[key])
			except:
				u += key + '=' + urllib.quote_plus(d[key].encode('utf-8'))
			i += 1
		return u