import sys
sys.path.append('/Users/mh/Downloads/beautifulsoup4-4.3.2/build/lib')
from bs4 import BeautifulSoup


before="""
<div class="separator" style="clear: both; text-align: center;">
<a href="http://3.bp.blogspot.com/-zLnBfsJh9zE/TVrAMEA5G5I/AAAAAAAAAXw/4nVUGy8oxII/s1600/P1000768.JPG" imageanchor="1" style="margin-left: 1em; margin-right: 1em;"><img border="0" src="http://3.bp.blogspot.com/-zLnBfsJh9zE/TVrAMEA5G5I/AAAAAAAAAXw/4nVUGy8oxII/s320/P1000768.JPG" height="240" width="320" /></a></div>

<div class="separator" style="clear: both; text-align: center;">
<a href="http://3.bp.blogspot.com/-HvZgpexyF28/TVrATKLGzyI/AAAAAAAAAX0/1f8Pa0ckIbY/s1600/P1000774.JPG" imageanchor="1" style="margin-left: 1em; margin-right: 1em;"><img border="0" src="http://3.bp.blogspot.com/-HvZgpexyF28/TVrATKLGzyI/AAAAAAAAAX0/1f8Pa0ckIbY/s320/P1000774.JPG" height="240" width="320" /></a></div>

<div class="separator" style="clear: both; text-align: center;">
<a href="http://1.bp.blogspot.com/-vOgBLzCjVfM/TVrAY3WWFEI/AAAAAAAAAX4/Q2NGFvN4keM/s1600/P1000788.JPG" imageanchor="1" style="margin-left: 1em; margin-right: 1em;"><img border="0" src="http://1.bp.blogspot.com/-vOgBLzCjVfM/TVrAY3WWFEI/AAAAAAAAAX4/Q2NGFvN4keM/s320/P1000788.JPG" height="240" width="320" /></a></div>

<div class="separator" style="clear: both; text-align: center;">
<a href="http://4.bp.blogspot.com/-OZfbQVLizy8/TVrAeBpK9oI/AAAAAAAAAX8/L3w79eCfUOs/s1600/P1000789.JPG" imageanchor="1" style="margin-left: 1em; margin-right: 1em;"><img border="0" src="http://4.bp.blogspot.com/-OZfbQVLizy8/TVrAeBpK9oI/AAAAAAAAAX8/L3w79eCfUOs/s320/P1000789.JPG" height="240" width="320" /></a></div>

<div class="separator" style="clear: both; text-align: center;">
<a href="http://3.bp.blogspot.com/-fZRYAy2xR_I/TVrAkNiDkfI/AAAAAAAAAYA/kZwzKUrm6l0/s1600/P1000790.JPG" imageanchor="1" style="margin-left: 1em; margin-right: 1em;"><img border="0" src="http://3.bp.blogspot.com/-fZRYAy2xR_I/TVrAkNiDkfI/AAAAAAAAAYA/kZwzKUrm6l0/s320/P1000790.JPG" height="240" width="320" /></a></div>
"""

after="""
<div class="separator" style="clear: both; text-align: center;">
<a href="http://3.bp.blogspot.com/-zLnBfsJh9zE/TVrAMEA5G5I/AAAAAAAAAXw/4nVUGy8oxII/s1600/P1000768.JPG" imageanchor="1" style="clear: left; float: left; margin-bottom: 1em; margin-right: 1em;"><img border="0" src="http://3.bp.blogspot.com/-zLnBfsJh9zE/TVrAMEA5G5I/AAAAAAAAAXw/4nVUGy8oxII/s320/P1000768.JPG" height="150" width="200" /></a></div>

<div class="separator" style="clear: both; text-align: center;">
<a href="http://3.bp.blogspot.com/-HvZgpexyF28/TVrATKLGzyI/AAAAAAAAAX0/1f8Pa0ckIbY/s1600/P1000774.JPG" imageanchor="1" style="clear: right; float: right; margin-bottom: 1em; margin-left: 1em;"><img border="0" src="http://3.bp.blogspot.com/-HvZgpexyF28/TVrATKLGzyI/AAAAAAAAAX0/1f8Pa0ckIbY/s320/P1000774.JPG" height="150" width="200" /></a></div>

<div class="separator" style="clear: both; text-align: center;">
<a href="http://1.bp.blogspot.com/-vOgBLzCjVfM/TVrAY3WWFEI/AAAAAAAAAX4/Q2NGFvN4keM/s1600/P1000788.JPG" imageanchor="1" style="margin-left: 1em; margin-right: 1em;"><img border="0" src="http://1.bp.blogspot.com/-vOgBLzCjVfM/TVrAY3WWFEI/AAAAAAAAAX4/Q2NGFvN4keM/s320/P1000788.JPG" height="240" width="320" /></a></div>

<div class="separator" style="clear: both; text-align: center;">
<a href="http://4.bp.blogspot.com/-OZfbQVLizy8/TVrAeBpK9oI/AAAAAAAAAX8/L3w79eCfUOs/s1600/P1000789.JPG" imageanchor="1" style="margin-left: 1em; margin-right: 1em;"><img border="0" src="http://4.bp.blogspot.com/-OZfbQVLizy8/TVrAeBpK9oI/AAAAAAAAAX8/L3w79eCfUOs/s320/P1000789.JPG" height="240" width="320" /></a></div>

<div class="separator" style="clear: both; text-align: center;">
<a href="http://3.bp.blogspot.com/-fZRYAy2xR_I/TVrAkNiDkfI/AAAAAAAAAYA/kZwzKUrm6l0/s1600/P1000790.JPG" imageanchor="1" style="margin-left: 1em; margin-right: 1em;"><img border="0" src="http://3.bp.blogspot.com/-fZRYAy2xR_I/TVrAkNiDkfI/AAAAAAAAAYA/kZwzKUrm6l0/s320/P1000790.JPG" height="240" width="320" /></a></div>
"""

diff="""
<a href="foo" imageanchor="1" style="clear: left; float: left; margin-bottom: 1em; margin-right: 1em;"><img border="0" height="150" src="foo" width="200"/></a>
<a href="foo" imageanchor="1" style="margin-left: 1em; margin-right: 1em;"><img border="0" height="240" src="foo" width="320"/></a>

<a href="foo" imageanchor="1" style="clear: left; float: left; margin-bottom: 1em; margin-right: 1em;"><img border="0" height="150" src="foo" width="200"/></a>
<a href="foo" imageanchor="1" style="margin-left: 1em; margin-right: 1em;">                            <img border="0" height="240" src="foo" width="320"/></a>
"""

search="""
<div class="separator">
<a>
<img />
</a>
</div>
"""


bsoup = BeautifulSoup(before)
asoup = BeautifulSoup(after)
print type(bsoup)

print '------'
print(bsoup.prettify())
print '------'
print(asoup.prettify())

print '------'
for i in asoup.find_all('img'):
    print i
print '------'
for i in bsoup.find_all('img'):
    print i


print '------'
for i in asoup.find_all('a'):
    print i
print '------'
for i in bsoup.find_all('a'):
    print i

print '------'
for i in asoup.select('div.separator > a > img'):
   print i.parent['style'] #img.get('src')

print '------'
for i in bsoup.select('div.separator > a > img'):
   print i.parent['style'] #img.get('src')
   i.parent['style']='style: foo;'


dirix=0
dirs=[["left","left","right"],["right","right","left"]]
replAstyle='clear: %s; float: %s; margin-bottom: 1em; margin-%s: 1em;'
print 999,dirs[dirix]
print 999,replAstyle%("left","left","right")

print '------'
for i in bsoup.select('div.separator > a > img'):
   print i.parent['style'] #img.get('src')

