from window import ChildWindow
from window import Container
from window import Window
from point import Point
import re
""" Unicode enabled text widget,"""
class TextBox(ChildWindow):
    def __init__(self, parent, title, top_left, w, h):
        #assert(parent is not None)
        #assert(isinstance(parent, (AppWindow)))
        #assert(isinstance(top_left, Point))
        if parent is None or not isinstance(parent, Container):
        	raise BadArgumentError("Expecting a valid parent window")
        
        Window.__init__(self, parent, title, top_left, w, h)
	self.text=None

    def setText(self, text):
    	self.text=text

    def getText(self):
    	return self.text

    def validate(self, validator):
    	validator(self.text)


def isaNumber(text):
	text=str(text)
	text=text.strip()
	if isaFloat(text)==True:
		return True
	a=re.search('[0-9]+',text)
	if a is not None:
		if len(text)==len(a.group()):
			return True
		return False
	else:
		return False

def isaFloat(text):
	text=str(text)
	text=text.strip()
	a=re.split('\.',text)
	if len(a)==2:
		b=re.search('[0-9]+',a[0])
		b =b.group()
		c=re.search('[0-9]+',a[1])
		c = c.group()
		if len(a[0])==len(b) and len(a[1])==len(c):
			return True
		return False
	else:
		return False

def isaURL(text):
	from urlparse import urlparse
	text=str(text)
	text=text.strip()
	a=urlparse(text)
	if a.scheme!="https" and a.scheme!="http":
		return False

	b=re.search('www\.',a.netloc)
	if b is not None:
		return True
	else:
		return False

