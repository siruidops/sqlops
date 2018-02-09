#!/bin/bash
# -*- coding: UTF-8 -*-

##                     In The Name Of God                             ##
#                                                                      #
# Subject  : Installer Script Sql Bug Scan & Sql Bug Seatch Dok Google #
# Time     : 2018-02-04 18:12                                          #
# Developer: Sir uidops                                                #
# Email    : Sir.u1d0p5@gmail.com                                      #
# Telegram : https://t.me/Sir_uidops                                   #
# Github   : https://github.com/uidops/sqlops                          #
#                                                                      #
##               Copy Right For Me (Sir Uidops)                       ##

# for errors in this script and help 
#    please send a message for me
#
# Email    : Sir.u1d0p5@gmail.com
# Telegram : https://t.me/Sir_uidops



apt-get update -y
clear


apt-get install git python python-dev python-pip -y
clear


pip install -r requ*.txt
clear


mkdir -p /opt/sqlops


cp run.sh /usr/bin/sqlops
cp update.py /usr/bin/sqlops-update
cp unistall.sh /usr/bin/sqlops-unistall


cp sqlops.py /opt/sqlops/
cp version.txt /opt/sqlops/
cp requ*.txt /opt/sqlops/
cp README.md /opt/sqlops/

echo 
echo " Installed In /opt/sqlops"
echo
echo " Unistalling With Command: 'sqlops-unistall'"
echo " Updateing   With Command: 'sqlopd-update'"
echo
echo "  Run this script using command: 'sqlops'"
echo