#!/home/dare/.virtualenvs/feedfilter/bin/python

import jinja2
import feedparser
import cgi
import settings
import cgitb
cgitb.enable(display=1, logdir="/home/dare/cgi/")

form = cgi.FieldStorage()
if 'visibility' in form:
	visibility = int(form['visibility'].value)
else:
	visibility = 49900
z = feedparser.parse(settings.FEED)
items = [item for item in z['items'] if 'visibility' in item and int(item['visibility']) > visibility]
#items = map(lambda item: item['summary'] = cgi.escape(item['summary']), items)
for item in items:
	item['summary'] = cgi.escape(item['summary'])
	item['published'] = item['published']
env = jinja2.Environment(loader=jinja2.FileSystemLoader("."))

#print items
#print
print "Content-Type: text/xml"
print
print env.get_template("feedtemplate.xml").render(items=items).encode('utf-8')
