from window import Window, Container, AppWindow,ChildWindow
from point import Point
from window import BadArgumentError

class DialogBox(Container, ChildWindow):
	#    STATE_ACCEPT = 0x4
#    STATE_CANCEL = 0x2
    def __init__(self, parent, title, top_left, w, h):
    	assert(parent is not None)
    	assert(isinstance(parent, (AppWindow)))
        assert(isinstance(top_left, Point))
#	self.states=None
    	self.STATE_ACCEPT = 0x4
    	self.STATE_CANCEL = 0x2
	self.state=self.STATE_ACCEPT
        Container.__init__(self, parent, title, top_left, w, h)

    def accept(self):
	self.state=self.STATE_ACCEPT

    def cancel(self):
	self.state=self.STATE_CANCEL

    def getState(self):
	return self.state


