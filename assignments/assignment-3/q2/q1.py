class DoublyLinkedList:
	class Node:
		def __init__(self,key,value):
			self._key=key
			self._value=value
			self._next=None
			self._prev=None

		def __eq__(self,key):
			return self._key==key

		def val(self):
			return self._value

	def __init__(self):
		self._head=None
		self._tail=None
		self._length=0
	
	def length(self):
		return self._length

	def insert(self,key,value):
		new_node=DoublyLinkedList.Node(key,value)
		if self._head == None:
			self._head=new_node
			self._tail=new_node
			self._head._prev=self._tail._next=None

		else:
			self._head._prev=new_node
			new_node._next=self._head
			self._head=new_node
		self._length+=1

	def PrintList( self ):
		node = self._head
		while node != None:
		        print node._key,node._value
			node = node._next
	
	def find(self,key):
		node=self._head
		while node!=None:
			if key == node._key:
				return node._value
			node=node._next
		return None

	def deleteLast(self):
		node = self._tail
		if self._head == None:
			print "List is empty"
			return

		elif self._length==1:	
			self._previous = self._next = self._head = self._tail = None
			self._length-=1
			return
		else:
			self._tail = node._prev
			self._tail._next = None
			node = self._tail
			self._length-=1

	def deleteFirst(self):
		node = self._head
		if self._head == None:
			print "List is empty"
			return

		elif self._length==1:	
			self._previous = self._next = self._head = self._tail = None
			self._length-=1
			return
		else:
			self._head = node._next
			self._head._prev=None
			node = self._head
			self._length-=1

	def delete(self,key):
		node=self._head
		if self._head == None:
			print "List is empty"
			return
		elif self._length == 1:
			if node._key == key:
				self._previous = self._next = self._head = self_tail = None
				self._length-=1
				return
			print 'Not Found'
			return
		else:
			count=0
			while node!=None:
				if node._key == key:
					self._length=self._length-1
					if count == 0:
						self._head=self._head._next
						self._head._prev=None
						return
					elif count==self._length - 1:
						self._tail=self._tail._prev
						self._tail._next=None
						return
					else:
						temp = node._next 
						node._next = temp._next
						node = temp._next._prev
						return
				node=node._next
				count+=1








