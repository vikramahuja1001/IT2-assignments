from q1 import DoublyLinkedList




def runListTests():
	def testEmptyList():
		l = DoublyLinkedList()
		assert(l.length() == 0)
	def testOneElementList():
	        l = DoublyLinkedList()
	        l.insert("name", "steve")
	        assert(l.find("name") == "steve")
	        assert(l.find("organization") is None)
	        l.deleteFirst()
	        assert(l.length() == 0)
        def testList():
                l = DoublyLinkedList()
	        l.insert("name", "steve")
	        assert(l.length() == 1)
		l.insert("name", "ken")
		assert(l.find("name") == "ken")
		l.insert("name", "rob")
		l.insert("name", "brian")
		assert(l.find("name") == "brian")
		assert(l.length() == 4)
		l.deleteFirst()
		assert(l.length() == 3)
		assert(l.find("name") == "rob")
	def testDeleteLast():
		l = DoublyLinkedList()
		l.deleteLast()
		assert(l.length() == 0)
		l.insert("name", "steve")
		l.deleteLast()
		assert(l.length() == 0)
		l.insert("name", "steve")
		l.insert("name", "ken")
		l.deleteLast()
		assert(l.length() == 1)
		assert(l.find("name") == "ken")
		l.deleteLast()
		assert(l.length() == 0)
		l.insert("name", "steve")
		l.insert("name", "ken")
		l.deleteLast()
		l.insert("name", "steve")
		assert(l.length() == 2)
		assert(l.find("name") == "steve")
	testEmptyList()
	testOneElementList()
	testList()
	testDeleteLast()
runListTests()




