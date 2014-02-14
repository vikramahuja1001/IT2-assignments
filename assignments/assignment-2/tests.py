from window import Window
from window import AppWindow
from window import Container
from window import ChildWindow

from textbox import TextBox
from textbox import isaNumber
from textbox import isaFloat
from textbox import isaURL

from dialogbox import DialogBox

from button import Button
from button import RadioButton
from button import RadioButtonGroup

from point import Point

def test_cases():
	#Tests for window.py
	def testWindow():
    		a1 = AppWindow("Test Application1", Point(10, 10), 200, 100)
	    	assert(a1.get_title() == "Test Application1")
    		assert(a1.get_size() == (200, 100))

		a2 = Container(None,"Test Application2", Point(200, 100), 10, 10)
		assert(a2.get_title() == "Test Application2")
    		assert(a2.get_size() == (10, 10))
		assert(a2.parent == None)
	
		assert(len(a1.children) == 0)
	
		a3 = Container(a1,"Test Application3", Point(0, 0), 20, 40)
    		assert(a3.get_title() == "Test Application3")
    		assert(a3.get_size() == (20, 40))
		assert(a3.parent == a1)
	
		#Creating CihldWindow for a1
		a4 = ChildWindow(a1,"Test Application4", Point(0, 0), 20, 40)
		a5 = ChildWindow(a1,"Test Application5", Point(0, 0), 20, 40)
		a6 = ChildWindow(a1,"Test Application6", Point(0, 0), 20, 40)
		a1.addChildWindow(a4)
		a1.addChildWindow(a5)
		a1.addChildWindow(a6)
	
		assert(len(a1.children) == 3)
	
	
		#Testing the ChildIterator class
		d=a1.childIterator()
		for i in d:
			print i
#		assert(d.next().get_title() == "Test Application4")
#		assert(d.next().get_title() == "Test Application5")
#		assert(d.next().get_title() == "Test Application6")
	
	
		#Testing the setFocus and hasFocus functions
		# Only one window has the focus at a time and it is the window which is most recently created
		assert(a1.hasFocus()==False)
		assert(a2.hasFocus()==False)
		assert(a3.hasFocus()==False)
		assert(a4.hasFocus()==False)
		assert(a5.hasFocus()==False)
		assert(a6.hasFocus()==True)
	
		assert(a3.setFocus()==True)
	
		assert(a1.hasFocus()==False)
		assert(a2.hasFocus()==False)
		assert(a3.hasFocus()==True)
		assert(a4.hasFocus()==False)
		assert(a5.hasFocus()==False)
		assert(a6.hasFocus()==False)
		
		#the app window when minimized is never in focus
		assert(a1.minimize()==True)
		assert(a1.setFocus()==False)
	
		assert(a1.hasFocus()==False)
		assert(a2.hasFocus()==False)
		assert(a3.hasFocus()==True)
		assert(a4.hasFocus()==False)
		assert(a5.hasFocus()==False)
		assert(a6.hasFocus()==False)
		#Testing the minimize and maximize functions
		
		#since a1 was already minimized so it did'nt minimize
		assert(	a1.minimize()==False)
	
		#When maximized a window automatically gets the focus
		assert(a5.maximize()==True)
		assert(a5.hasFocus()==True)
	
		#Only one window gets the focus at a time
		assert(a1.hasFocus()==False)
		assert(a2.hasFocus()==False)
		assert(a3.hasFocus()==False)
		assert(a4.hasFocus()==False)
		assert(a5.hasFocus()==True)
		assert(a6.hasFocus()==False)
	
	
	#Test for textbox.py
	def testTextbox():
		a1 = AppWindow("Test Application1", Point(0, 0), 20, 40)
		t1 = TextBox(a1,"Test Application2", Point(0, 0), 20, 40)
		t2 = TextBox(a1,"Test Application3", Point(0, 0), 20, 40)
		t3 = TextBox(a1,"Test Application4", Point(0, 0), 20, 40)
		# 3 textboxes t1,t2,t3 created with a1 as their parent
	
		assert(t1.getText()==None)
		assert(t2.getText()==None)
		assert(t3.getText()==None)
		#Initially all these have no texts in them
	
		t1.setText("427655638956876")
		assert(t1.getText() == "427655638956876")
		assert(isaNumber(t1.getText()) == True)
		assert(isaFloat(t1.getText()) == False)
		assert(isaURL(t1.getText()) == False)
		#	t1.validate(isaNumber(t1.getText()))
	
		t2.setText("427655638.956876")
		assert(t2.getText()=="427655638.956876")
		assert(isaNumber(t2.getText()) == True)
		assert(isaFloat(t2.getText()) == True)
		assert(isaURL(t2.getText()) == False)

		t3.setText("https://www.google.com")
		assert(t3.getText()=="https://www.google.com")
		assert(isaNumber(t3.getText()) == False)
		assert(isaFloat(t3.getText()) == False)
		assert(isaURL(t3.getText()) == True)

		t3.setText("http://www.google.com")
		assert(t3.getText()=="http://www.google.com")
		assert(isaNumber(t3.getText()) == False)
		assert(isaFloat(t3.getText()) == False)
		assert(isaURL(t3.getText()) == True)
	
	
	#test for dialogbox.py
	def testDialogBox():
		a1 = AppWindow("Test Application", Point(10, 10), 200, 100)
		dlg = DialogBox(a1, "Test Dialog", Point(100, 50), 50, 50)
		# a dialogbox dlg created with a1 as its parent window
		assert(dlg.get_title() == "Test Dialog")
		assert(dlg.get_size() == (50, 50))
	
		dlg.accept() #accepted the dialogbox dlg
		assert(dlg.getState() == dlg.STATE_ACCEPT)
	
		dlg.accept() #accepted the dialogbox dlg
		assert(dlg.getState() == dlg.STATE_ACCEPT)
	
		dlg.cancel() #canceled the dialogbox dlg
		assert(dlg.getState() == dlg.STATE_CANCEL)
	
		dlg.accept() #accepted the dialogbox dlg again
		assert(dlg.getState() == dlg.STATE_ACCEPT)
	
	
	def testButton():
		a1 = Container(None,"Test Application1", Point(10, 10), 200, 100)
		a2 = AppWindow("Test Application2", Point(10, 10), 200, 100)
		#Here 2 different parent windows a1 and a2 were created
	
		r1 = RadioButtonGroup(a1,"Test Application3", Point(10, 10), 200, 100)
		#r1 is the radiobuttongroup corresponding the parent Container a1
		r2 = RadioButtonGroup(a2,"Test Application4", Point(10, 10), 200, 100)
		#r2 is the radiobuttongroup corresponding the parent Container a2
	
	
		r11 = RadioButton(r1,"Test Application5", Point(10, 10), 200, 100)
		r12 = RadioButton(r1,"Test Application6", Point(10, 10), 200, 100)
		r13 = RadioButton(r1,"Test Application7", Point(10, 10), 200, 100)
		# r11,r12 and r13 are the 3 radiobuttons in the radiobuttongroup r1. Here r11,r12 and r13 are siblings
	
		r21 = RadioButton(r2,"Test Application8", Point(10, 10), 200, 100)
		r22 = RadioButton(r2,"Test Application9", Point(10, 10), 200, 100)
		r23 = RadioButton(r2,"Test Application10", Point(10, 10), 200, 100)
		# r21,r22 and r23 are the 3 radiobuttons in the radiobuttongroup r2. Here r21,r22 and r23 are siblings
	
		assert(r11.getState() == RadioButton.RADIO_ACTIVE)
		assert(r12.getState() == RadioButton.RADIO_INACTIVE)
		assert(r13.getState() == RadioButton.RADIO_INACTIVE)
		#When created by default the first radiobutton(r11) of the corresponding radiobuttongroup(r1) is selected
	
		assert(r21.getState() == RadioButton.RADIO_ACTIVE)
		assert(r22.getState() == RadioButton.RADIO_INACTIVE)
		assert(r23.getState() == RadioButton.RADIO_INACTIVE)
		#When created by default the first radiobutton(r21) of the corresponding radiobuttongroup(r2) is selected
	
		assert(r12.click() == True) # Since initialy r11 was selected , so now r12 is Active and r11 is Inactive 
		assert(r12.click() == False) # r12 was Active and when it was clicked again , it returned false
	
		assert(r11.getState() == RadioButton.RADIO_INACTIVE)
		assert(r12.getState() == RadioButton.RADIO_ACTIVE)
		assert(r13.getState() == RadioButton.RADIO_INACTIVE)
		# Only r12 is Active in the radiobuttongroup r1
		
		assert(r21.click()  == False)# r21 being initiall selected returned False on .click()
		
		assert(r21.getState() == RadioButton.RADIO_ACTIVE)
		assert(r22.getState() == RadioButton.RADIO_INACTIVE)
		assert(r23.getState() == RadioButton.RADIO_INACTIVE)
		#r21 is the still Active in the radiobuttongroup r2
	
	
	testWindow()
	testTextbox()
	testDialogBox()
	testButton()
test_cases()
