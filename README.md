blogger-tools
=============

Tools for interacting with blogger/blogspot

blogger-tools
-------------

Simple filters, etc for use when typing blog posts

decolor -- sometimes you copy and paste text into a blog that has hard-coded coloring.  this strips it out.  Typical use:

- switch to html view
- select all text
- in terminal window: decolor pb
- paste

blogix -- indexing tools
------------------------

This set of programs generates various flavors of indices and
tables of contents for blogspot sites.

processing flow:

- downloads xml dump of blog
- digest xml into sqlite
- generate files, based upon metadata labels in each post
- upload files to pre-defined pages on blog (not done, can be done manually)

specific steps:

- ./fetch
- ./digest blog.xml
- ./gen
- cleanup:  rm *.html blog.db blog.xml
- I use make for this... there's a sample Makefile you can customize.

configuration:

$HOME/.blogixrc sets 3 items: feed id, gmail logon, and password.
Get your feed number from here:
http://support.google.com/blogger/bin/answer.py?hl=en&answer=42191

    FEED=12312312312312312  
    GMAIL=mymail@gmail.com
    echo google passwd:
    stty -echo
    read GPASS
    stty echo

todo:
- automate upload step
- use config file to drive generation
- add sample pages
- see if there are any other indices that are useful

scad-demos
----------

Two things here:

- a set of demos for SCAD coding.  Is this really a blogger tool?
  Maybe it is, it certainly seems a blogworthy topic.

- some code to break apart several scad programs.  An "mscad"
  file is a series of scad files, separated by lines of 72 hyphens.
  The program breaks them apart, generates an image for each scad
  program, and wraps it all in an html table.  It would be nice for
  it to wrap in a blogger friendly way, then it would be easy to
  write a tutorial style blog post.
