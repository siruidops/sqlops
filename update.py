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

red="\033[0;31m"
green="\033[0;32m"
brown="\033[0;33m"
blue="\033[0;34m"
tur="\033[1;36m"
yellow="\033[1;33m" 
end="\033[1;37m"
pur="\033[0;35m" 

import os, sys, urllib

print
print green+"[+] Updating SqlOps Tool ..."+end
print
try:
	u = urllib.urlopen('$URL')
except:
	print
	print red+" [-] Not cant connect to github site"+end
	print
	sys.exit()
if '1.0' in u.read():
	print " [!] New Update Find: "+u.read().strip()
	print
	res = raw_input('update > Confirm _ [Y]es, [n]o >>> ')
	if 'y' in res or 'Y' in res:
		os.chdir('/root/')
		f = 'sqlops-update-',u.read().strip()
		os.mkdir(f)
		os.chdir(f)
		os.system('git clone https://github.com/uidops/sqlops.git')
		os.system('sqlops-unistall')
		os.chdir('sqlops')
		os.system('./install.sh')
		os.system('clear')
		print
		print tur," *------------------------------*",end
		print green,"    Updated !",end
		print
		print green,"    Name   : SqlOps",end
		print green,"    Version: ",u.read().strip(),end
		print tur," *------------------------------*"
		print
	else:
		print
		sys.exit()

else:
	print
	print " [+] Updated ! "
	print






