# logger
Attempt at Administrative tool set with python
Author: Luisito M. Pena.
Date: 4/16/16
Purpose: Attempt to create an all puprpose RAT;
The goal is to have it run any any flavor and desktop known to GNU/Linux.
Note: as of 4/16, I am binding a shell script to handle installing the
programs needed to get this thing to work, like a VNC. This can change later.
Very well then, here I go.

# using pyxhook, All credit goes to original author 
" Copyright (C) 2008 Tim Alexander <dragonfyre13@gmail.com> "

#Requirements
python-xlib needs to be installed. This is a python2 lib. required by pyxhook
Fedora 23+: dnf install python-xlib
Redhat, Fedora -23: yum install python-xlib
Debian/ubuntu based: apt-get install python-xlib
Arch: pacman -S python2-xlib, In AUR there is a python 3 Port
Gentoo : emrge --ask dev-python/python-xlib

The Xorg module libxcb-record.so needs to be enabled
Fedora 23+ x86_64: /usr/lib64/libxcb-record.so
enable in /usr/X11/xorg.conf

Lastly, Make the python module
" Image " is installed. 

