
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

