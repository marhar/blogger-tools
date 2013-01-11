#!/bin/sh
#
# doit -- download today's blog export and put it into blog.db
# 
# 1. download current blog export
# 2. import into blog.db
# 3. generate html
# 4. upload html [to be completed]

all: clean
	./fetch
	./digest blog.xml
	./gen
	echo TODO ./upload

clobber: clean
	rm -f blog.db
	rm -f blog.xml

clean:
	rm -f *.html
