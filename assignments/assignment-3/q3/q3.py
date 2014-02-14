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
	def __init__(self,lbp,w,h):
		self.lbp=Point(lbp[0],lbp[1]);
		self.w=w;
		self.h=h;
	def intersect(self,other):				#[for self 1 mark, rest function 6.5]
		x1 = self.lbp.x
		x2 = other.lbp.x
		y1 = self.lbp.y
		y2 = other.lbp.y
		w1 = self.w
		w2 = other.w
		h1 = self.h
		h2 = other.h
		X = (((x1<=x2) and (x2<=(x1+w1))) or ((x2<=x1) and (x1<=(x2+w2))))
		Y = (((y1<=y2) and (y2<=(y1+h1))) or ((y2<=y1) and (y1<=(y2+h2))))
		if ( X and Y):
			return True
		else:
			return False


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



