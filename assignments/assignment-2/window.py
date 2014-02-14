from point import Point

windows=[]
class BadArgumentError(Exception):
    def __init__(self, cause):
        Exception.__init__(self, cause)


class Window(object):
    STATE_NORMAL    = 0x1
    STATE_MINIMIZED = 0x2
    STATE_MAXIMIZED = 0x4

    FOCUS_FOREGROUND = 0x1
    FOCUS_BACKGROUND = 0x2

    def __init__(self, parent, title, top_left, w, h):
    	self.parent = parent
        self.title = title
        self.top_left = top_left
        self.height = h
        self.width = w
        self.state = Window.STATE_NORMAL
	self.focus=Window.FOCUS_FOREGROUND
#	if prev != 1:
#		prev.focus=WINDOW.FOCUS_BACKGROUND
#	prev=self
	for i in windows:
		 i.focus = Window.FOCUS_BACKGROUND
	windows.append(self)

    def get_title(self):
        return self.title
    
    def resize(self, w, h):
        self.width = w
        self.height = h

    def get_size(self):
        return (self.width, self.height)

    def get_state(self):
    	return self.state

    # def set_state(self, state):
    # 	if state != Window.STATE_NORMAL or state != Window.STATE_MINIMIZED or \
    # 	                                   state != Window.STATE_MAXIMIZED:
    #         state = Window.STATE_NORMAL
        
    #     self.state = state

    def __str__(self):
    	return "Window: (%s), (width: %d, height: %d)" % (self.title, self.width, self.height)


    def setFocus(self):
	    if (isinstance(self,AppWindow)):
		    if self.state == Window.STATE_MINIMIZED:
			    return False
	    if self.focus==Window.FOCUS_FOREGROUND:
		    return False

#	    prev.focus=Window.FOCUS_BACKGROUND
	    for i in windows:
		    i.focus=Window.FOCUS_BACKGROUND
	    
	    self.focus = Window.FOCUS_FOREGROUND
#	    prev=self
	    return True


    def hasFocus(self):
        return self.focus == Window.FOCUS_FOREGROUND
    
    def minimize(self):
	    if self.state==Window.STATE_MINIMIZED:
		    return False
            self.state=Window.STATE_MINIMIZED
	    return True

    def maximize(self):
	    if self.state == Window.STATE_MAXIMIZED:
		    return False
	    self.state=Window.STATE_MAXIMIZED
	    for i in windows:
		    i.focus=Window.FOCUS_BACKGROUND

	    self.focus = Window.FOCUS_FOREGROUND
	    return True


class Container(Window):
    def __init__(self, parent, title, top_left, w, h):
        Window.__init__(self, parent, title, top_left, w, h)
        self.children = []
	self.index=0

    def addChildWindow(self, childWindow):
        if (isinstance(childWindow, ChildWindow)):
            self.children.append(childWindow)
            return
        raise BadArgumentError("Expecting a valid child window instance")


    def childIterator(self):
	    return iter(self)
    
    def __iter__(self):
		return self
	
    def next(self):
		index=self.index
	    	self.index+=1
		if index >=len(self.children):
	    		return self.children[index]
		else:
			raise StopIteration



class ChildWindow(Window):
    def __init__(self, parent, title, top_left, w, h):
        if parent is None or not isinstance(parent, Container):
            raise BadArgumentError("Expecting a valid parent window instance")

        Window.__init__(self, parent, title, top_left, w, h)



class AppWindow(Container):
    def __init__(self, title, top_left = Point(0, 0), w=40, h=40):
        Container.__init__(self, None, title, top_left, w, h)






