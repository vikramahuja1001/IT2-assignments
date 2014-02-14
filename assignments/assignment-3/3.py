import re


#a

#rectangle class
class point:
	def __init__(self,x,y):
		self.x=x
		self.y=y

	def __str__(self):
	        return "(x: %f, y: %f)" % (self.x, self.y)


class Rectangle:
	def __init__(self,lbp,width,height):
		self.lbp=lbp
		self.width=width
		self.height=height

#def check_colln(r1,r2):
	#check collision

	

# part b

class WordIterator:
	def __init__(self,text):
		self.text=re.split(' ',text)
		self.index=0

	def __iter__(self):
		return self

	def next(self):
		try:
			self.index+=1
			return self.text[self.index-1]
		except IndexError:
			raise StopIteration



#part c
class PointIterator:
	def __init__(self,p1,p2,n):
		self.p1=p1
		self.p2=p2
		self.n=n
		self.x=(max(self.p1.x,self.p2.x)-min(self.p1.x,self.p2.x))/(self.n * 1.0)
		self.y=(max(self.p1.y,self.p2.y)-min(self.p1.y,self.p2.y))/(self.n * 1.0)


	def __iter__(self):
		return self

	def next(self):
		a1=self.p1
		a1.x=(1.0 * a1.x)+self.x
		a1.y=(1.0 * a1.y)+self.y
		return a1

	
def max(a1,a2):
	if a1 >= a2 :
		return a1
	else: return a2

def min(a1,a2):
	if a1 <= a2 :
		return a1
	else: return a2




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
