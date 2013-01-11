blogger-tools
=============

Tools for interacting with blogger/blogspot

blogix -- indexing tools
------------------------

This set of programs generates various flavors of indices and
tables of contents for blogspot sites.

processing flow:

- downloads xml dump of blog (not done, needs blogger api addition)
- digest xml into sqlite
- generate files, based upon metadata labels in each post
- upload files to pre-defined pages on blog (not done, can be done manually)

specific steps:

- download xml dump from admin menu: settings/other/export blog
- ./digest blog-01-10-2013.xml
- ./gen
- cleanup:  rm *.html blog.db blog.xml

todo:
- automate download, upload steps
- use config file to drive generation
- add sample pages
- see if there are any other indices that are useful
