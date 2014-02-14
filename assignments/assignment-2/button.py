from window import ChildWindow
from window import Container
from window import AppWindow
from window import Window
from point import Point
from window import BadArgumentError

class Button(ChildWindow):
    def __init__(self, parent, title, top_left, w, h):
        #assert(parent is not None)
        #assert(isinstance(parent, (AppWindow)))
        #assert(isinstance(top_left, Point))
        if parent is None or not isinstance(parent, Container):
        	raise BadArgumentError("Expecting a valid parent window")
        
        Window.__init__(self, parent, title, top_left, w, h)

    def click(self):
    	raise NotImplementedError()


class OK(Button):
	    def __init__(self, parent, title, top_left, w, h):
		    Button.__init__(self, parent, title, top_left, w, h)

	    def click(self):
		    self.parent.accept()
		    return True
    
class Cancel(Button):
	    def __init__(self, parent, title, top_left, w, h):
		    Button.__init__(self, parent, title, top_left, w, h)

	    def click(self):
		    self.parent.cancel()
		    return True


class RadioButton(Button):
	RADIO_ACTIVE   = 0x1
	RADIO_INACTIVE = 0x2
	def __init__( self, parent, title, top_left, w, h):
		if parent is None or not isinstance(parent,RadioButtonGroup):
        		raise BadArgumentError("Expecting a valid parent window")
		
		Button.__init__(self, parent, title, top_left, w, h)
		if self.parent.count == 0:
			self.radio_state=RadioButton.RADIO_ACTIVE
		else:
			self.radio_state=RadioButton.RADIO_INACTIVE
		self.parent.count+=1
		parent.RadioChildren.append(self)

	def click(self):
		if self.radio_state == RadioButton.RADIO_ACTIVE:
			return False
		for i in self.parent.RadioChildren:
			i.radio_state=RadioButton.RADIO_INACTIVE
		self.radio_state=RadioButton.RADIO_ACTIVE
		return True


	def getState(self):
		return self.radio_state


class RadioButtonGroup(Container):
	def __init__(self, parent, title, top_left, w, h):
		Container.__init__(self, parent, title, top_left, w, h)
		self.RadioChildren=[]
		self.count=0

