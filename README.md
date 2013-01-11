blogger-tools
=============

Tools for interacting with blogger/blogspot

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

todo:
- automate upload step
- use config file to drive generation
- add sample pages
- see if there are any other indices that are useful
