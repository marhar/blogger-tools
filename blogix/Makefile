#!/bin/sh
#
# doit -- download today's blog export and put it into blog.db
# 
# 1. download current blog export [now just copies from ~/Downloads]
# 2. import into blog.db
# 3. generate html
# 4. upload html [to be completed]


all: clean
	
	echo TODO ./download
	mv $(HOME)/Downloads/blog-`date +%m-%d-%Y`.xml .
	./digest blog-`date +%m-%d-%Y`.xml
	./gen
	echo TODO ./upload

clobber: clean
	rm -f blog.db
	rm -f blog-`date +%m-%d-%Y`.xml

clean:
	rm -f *.html
