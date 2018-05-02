import sys
import os
import urllib
import xbmc
import xbmcgui
import xbmcplugin
import xbmcaddon
import logging
from operator import itemgetter

def show_streams():
  stream_handle = int(sys.argv[1])
  xbmcplugin.setContent(stream_handle, 'tvshows')
  for stream in LiveTV:
    iconPath = os.path.join(home, 'logos', stream['icon'])
    li = xbmcgui.ListItem(stream['name'], iconImage=iconPath)
    xbmcplugin.addDirectoryItem(handle=stream_handle, url=stream['url'], listitem=li)

  xbmcplugin.endOfDirectory(stream_handle)

addon = xbmcaddon.Addon()
home = xbmc.translatePath(addon.getAddonInfo('path'))

LiveTV = [
  { 'name': 'Canal 2', 'url': 'http://138.117.4.70:8079/streams/d/Canal-2/playlist.m3u8', 'icon': 'canal_2.png' },
  { 'name': 'Canal 4', 'url': 'http://138.117.4.70:8079/streams/d/Canal-4/playlist.m3u8', 'icon': 'canal_4.png' },
  { 'name': 'Canal 6', 'url': 'http://138.117.4.70:8079/streams/d/Canal-6/playlist.m3u8', 'icon': 'canal_6.png' },
  { 'name': 'Canal 8', 'url': 'http://138.117.4.70:8079/streams/d/Canal-25/playlist.m3u8', 'icon': 'canal_8.png' },
  { 'name': 'Canal 9', 'url': 'http://138.117.4.70:8079/streams/d/Canal-9/playlist.m3u8', 'icon': 'canal_9.png' },
  { 'name': 'Canal 10', 'url': 'http://138.117.4.70:8079/streams/d/Canal-10/playlist.m3u8', 'icon': 'canal_10.png' },
  { 'name': 'Canal 11', 'url': 'http://138.117.4.70:8079/streams/d/Canal-11/playlist.m3u8', 'icon': 'canal_11.png' },
  { 'name': 'Canal 12', 'url': 'http://138.117.4.70:8079/streams/d/Canal-12/playlist.m3u8', 'icon': 'canal_12.png' },
  { 'name': 'Canal 13', 'url': 'http://138.117.4.70:8079/streams/d/Canal-13/playlist.m3u8', 'icon': 'canal_13.png' },
  { 'name': 'Canal 15', 'url': 'http://138.117.4.70:8079/streams/d/Canal-15/playlist.m3u8', 'icon': 'canal_15.png' },
  { 'name': 'Canal 17', 'url': 'http://138.117.4.70:8079/streams/d/Canal-17/playlist.m3u8', 'icon': 'canal_17.png' },
  { 'name': 'Canal 21', 'url': 'http://138.117.4.70:8079/streams/d/Canal-21/playlist.m3u8', 'icon': 'canal_21.png' },
  { 'name': 'Canal 23', 'url': 'http://138.117.4.70:8079/streams/d/Canal-23/playlist.m3u8', 'icon': 'canal_23.png' },
  { 'name': 'Canal 39', 'url': 'http://138.117.4.70:8079/streams/d/Canal-39/playlist.m3u8', 'icon': 'canal_39.png' },
  { 'name': 'Granada', 'url': 'http://138.117.4.70:8079/streams/d/Granada/playlist.m3u8', 'icon': 'granada.png' },
  { 'name': 'EWTN', 'url': 'http://StreamCdnC2.mainstreaming.tv:80/cdn/live/101129/vYhEBFa/chunklist_b732000.m3u8', 'icon': 'ewtn.png' },
  { 'name': 'RT', 'url': 'http://138.117.4.70:8079/streams/d/RT/playlist.m3u8', 'icon': 'rt.png' },
  { 'name': 'Hispan TV', 'url': 'http://138.117.4.70:8079/streams/d/hispan/playlist.m3u8', 'icon': 'hispan_tv.png' },
  { 'name': 'CNN-ESPA', 'url': 'http://138.117.4.70:8079/streams/d/CNN-ESPA/playlist.m3u8', 'icon': 'cnn.png' }
]

show_streams()