from q3 import *



def test_cases():

	def test_for_WordIterator():
		a1=WordIterator('This is the second question of the 3rd itws assignment')
		b=iter(a1)
		assert(b.next()=='This')
		assert(b.next()=='is')
		assert(b.next()=='the')
		assert(b.next()=='second')
		assert(b.next()=='question')
		assert(b.next()=='of')
		assert(b.next()=='the')
		assert(b.next()=='3rd')
		assert(b.next()=='itws')
		assert(b.next()=='assignment')
	
	def test_for_PointIterator():
		p1=point(10,20)
		p2=point(100,200)
		n=13
		p=PointIterator(p1,p2,n)
		a=iter(p)
		for i in range(n):
			print a.next()


	test_for_WordIterator()
	test_for_PointIterator()
test_cases()
