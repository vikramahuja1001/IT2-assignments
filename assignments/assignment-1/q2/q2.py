def length(vector):
	p1,p2 =vector
	x1,y1,z1=p1
	x2,y2,z2=p2
	lengths=((x1-x2)*(x1-x2))+((y1-y2)*(y1-y2))+((z1-z2)*(z1-z2))
	return (lengths)**0.5


def normalize(vector):
	p1,p2=vector
	x1,y1,z1=p1
	x2,y2,z2=p2
	x=p1[0]-p2[0]
	y=p1[1]-p2[1]
	z=p1[2]-p2[2]
	denom = (x*x + y*y + z*z) ** 0.5
	x2=x2/denom
	y2=y2/denom
	z2=z2/denom
	p2=(x2,y2,z2)
	p1=(0,0,0)
	vector=(p1,p2)
	return vector


def dot_product(vector1,vector2):
	p1,p2=vector1
	p3,p4=vector2
	a1 = p1[0] - p2[0]
	b1 = p1[1] - p2[1]
	c1 = p1[2] - p2[2]
	a2 = p3[0] - p4[0]
	b2 = p3[1] - p4[1]
	c2 = p3[2] - p4[2]
	return (a1*a2)+(b1*b2)+(c1*c2)


def cross_product(vector1,vector2):
	p1,p2=vector1
	p3,p4=vector2
	x1=p1[0] - p2[0]
	y1=p1[1] - p2[1]
	z1=p1[2] - p2[2]
	x2=p3[0] - p4[0]
	y2=p3[1] - p4[1]
	z2=p3[2] - p4[2]
	c1=(y1*z2) - (z1*y2)
	c2=(z1*x2) - (x1*z2)
	c3=(x1*y2) - (y1*x2)
	p1=(0,0,0)
	p2=(c1,c2,c3)
	vector=(p1,p2)
	return vector

