#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Tested on Windows, Linux, Android

##               In The Name Of God                  ##
#                                                     #
# Subject  : Sql Bug Scan & Sql Bug Seatch Dok Google #
# Time     : 2018-02-04 18:12                         #
# Developer: Sir uidops                               #
# Email    : Sir.u1d0p5@gmail.com                     #
# Telegram : https://t.me/Sir_uidops                  #
# Github   : https://github.com/uidops                #
#
##         Copy Right For Me (Sir Uidops)            ##

# for errors in this script and help 
#    please send a message for me
#
# Email    : Sir.u1d0p5@gmail.com
# Telegram : https://t.me/Sir_uidops

# Colors ['red', 'green', 'brown', 'blue', 'turquoise', 'yellow', 'white', 'purple']
red="\033[0;31m"
green="\033[0;32m"
brown="\033[0;33m"
blue="\033[0;34m"
tur="\033[1;36m"
yellow="\033[1;33m" 
end="\033[1;37m"
pur="\033[0;35m" 

# import librares ['requests', 'sys', 'os' ,'getopt', 'html5lib', 'bs4']
import requests
import sys
import os
import getopt

# Design Logo For This Tool
logo = yellow+"""
             _/_/_/         _/     _/_/_/_/       _/_/_/
              _/    _/_/_/ _/     _/    _/ _/_/_/  _/
               _/  _/  _/ _/     _/    _/ _/  _/    _/
           _/_/_/ _/_/_/ _/     _/_/_/_/ _/_/_/ _/_/_/
                     _/                 _/
                    _/                 _/    1.0
                   _/                 _/
"""+end

# Creat Banner 
def banner():
	print 
	print logo
	print
	print tur+"Developer"+end+': '+pur+"Sir uidops"+end
	print tur+"Email    "+end+': '+pur+"Sir.u1d0p5@gmail.com"+end
	print tur+"Telegram "+end+': '+pur+"https://t.me/Sir_uidops"+end
	print
	print yellow+"Options"+end
	print
	print tur+"    -f   "+end+': '+pur+"File url to scan"+end
	print tur+"    -u   "+end+': '+pur+"Single url to scan"+end
	print tur+"    -s   "+end+': '+pur+"Scan Sql Bug Using Google Dork"+end
	print tur+"    -r   "+end+': '+pur+"Show README.md File"+end
	print tur+"    -h   "+end+': '+pur+"Show Help Banner"+end
	print
	print yellow+"Example"+end
	print
	print pur+"    ./sqlops.py "+tur+"-f "+green+"url.txt"+end
	print pur+"    ./sqlops.py "+tur+"-u "+green+"http://example.com/index.php?id=4"+end
	print pur+"    ./sqlops.py "+tur+"-s "+green+"'inurl:index.php?id='"+end
	print pur+"    ./sqlops.py "+tur+"-h"+end
	print

# App File
def file(fileName):
	try:
		fo = open(fileName, "r")
		words = fo.readlines()
		fo.close()
		print
		print tur+" [!] Scanning {} url in file {}\033[1;37m".format(len(words), fileName)
		print
	except IOError:
		print
		print red+" [-] Not cant open the your url file: ",fileName
		print
		sys.exit()
	for url in words:
		url = url.strip()
		site = "%s'"%(url)
		try:
			req = requests.post(site).content
		except:
			print red+" [-] Request Time Out"+end
			req = ""
		if 'SQL syntax' in req:
			print green+" [+] Sucess => "+url+end
		else:
			pass

# All Signle
def single(sqlurl):
	url = sqlurl
	url = url.strip()
	site = "%s'"%(url)
	print
	try:
		req = requests.post(site).content
	except:
		print red+" [-] Request Time Out"+end
		req = ""
	if 'SQL syntax' in req:
		print green+" [+] Success => "+url+end
	else:
		print red+" [-] Try => "+url+end

# App Search
def search(dork):
	try:
		from googlesearch import search as Search
	except ImportError:
		print
		print red+" [-] Please install 'google' library"
		print green+"     : pip install google"
		print
		sys.exit()
	print
	try:
		bin = Search(dork)
	except:
		print " [-] Request Time Out"
	for i in bin:
		print i

# App
def app():
	argv = sys.argv[1:]
	if len(sys.argv) == 1:
		banner()
		sys.exit()
	else:
		pass
	if len(sys.argv) > 3:
		banner()
		print "\t"+red+"[-] Invalid Options"+end
		sys.exit('\n')
	else:
		pass
	try:
		opts, args = getopt.getopt(argv, '-f:-u:-s:-h-r')
	except:
		banner()
		sys.exit()
	for opt,arg in opts:
		if opt == '-f':
			file(arg)
			sys.exit('\n')
		elif opt == '-u':
			single(arg)
			sys.exit('\n')
		elif opt == '-s':
			search(arg)
			sys.exit('\n')
		elif opt == '-h':
			banner()
			sys.exit()
		else:
			banner()
			sys.exit()

# Check For Run Script
if __name__ == "__main__":
	app()
else:
	sys.exit()















