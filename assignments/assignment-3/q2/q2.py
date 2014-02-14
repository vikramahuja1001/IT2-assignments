from q1 import *
class ForwardListIterator(DoublyLinkedList): 
	def __init__(self):
		DoublyLinkedList.__init__(self)
		    
	def __iter__(self):
		return DoublyLinkedlist.head
	 
	def next(self):
		if self.next:
			return self.next
		raise StopIteration
		
		
class BackwardListIterator(DoublyLinkedList):
	def __init__(self):
		DoublyLinkList.__init__(self)
	 
	def __iter__(self):
		return DoublyLinkedList.tail
		 
	def next(self):
		if self.prev:
			return self.prev
		raise StopIteration

class IterableDoublyLinkedList(DoublyLinkedList):				
	    class ReverseIterator(object):
		def __init__(self, node):
		    self.next_node = node
		
		def next(self):				
		    if self.next_node is not None:
			    val = self.next_node.val()
			    self.next_node = self.next_node.getPrev()
			    return val
		    else:
			    raise StopIteration()
		def getReverseIterator(self):	
			return IterableDoublyLinkedList.ReverseIterator(self.tail)
