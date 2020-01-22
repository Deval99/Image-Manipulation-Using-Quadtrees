import math
#for storing a cartesian point 
class point:
	def __init__(self, iX, iY):
		self.iX = iX
		self.iY = iY
#to store a node
class node:
	def __init__(self, data, point):
		self.data = data
		self.point = point

def inorder(quad, mlist):
	#print "\nSTART"
	if hasattr(quad, 'topLeftChild'):
		#print "has topLeft"
		inorder(quad.topLeftChild, mlist)
	if hasattr(quad, 'topRightChild'):
		#print "has topright"
		inorder(quad.topRightChild, mlist)
	if hasattr(quad, 'botLeftChild'):
		#print "has botLeft"
		inorder(quad.botLeftChild, mlist)
	if hasattr(quad, 'botRightChild'):
		#print "has botRight"
		inorder(quad.botRightChild, mlist)
	if hasattr(quad, 'node'):	
		mlist.append(quad.node.data)
		#print(quad.node.data, "--", quad.node.point.iX,",",quad.node.point.iY);
	#print "RETURN"

#for storing a quad
class quad:
	def __init__(self, TLpoint, BRpoint, iC):
		self.TLpoint = TLpoint
		self.BRpoint = BRpoint 
		self.iC=0
	def add(self, apoint, data):
		self.BRpoint.iX = int(self.BRpoint.iX)
		self.BRpoint.iY = int(self.BRpoint.iY)
		self.TLpoint.iX = int(self.TLpoint.iX)
		self.TLpoint.iY = int(self.TLpoint.iY)
		#print("tl(",self.TLpoint.iX,",",self.TLpoint.iY,")","br(",self.BRpoint.iX,",",self.BRpoint.iY,")","point(",apoint.iX,",",apoint.iY,")")
		#print("DBUG9(",self.BRpoint.iX,",",self.BRpoint.iY,")")
		#print("DBUG99 ",apoint.iX, ",", apoint.iY)
		if self.checkBoundry(apoint):
			print("OutOfRange!")
			print("tl(",self.TLpoint.iX,",",self.TLpoint.iY,")","br(",self.BRpoint.iX,",",self.BRpoint.iY,")","point(",apoint.iX,",",apoint.iY,")")
			#exit()
			return
		if ((self.BRpoint.iX - self.TLpoint.iX) <= 1) or ((self.BRpoint.iY - self.TLpoint.iY) <= 1):
			
			#print("LessThan1", "(",self.TLpoint.iX,",",self.TLpoint.iY,")","-","(",self.BRpoint.iX,",",self.BRpoint.iY,")")
			self.node = node(data, apoint)
			#print("Node Added ! at ","(",self.TLpoint.iX,",",self.TLpoint.iY,")","(",self.BRpoint.iX,",",self.BRpoint.iY,")")
			#print "Node Added !"
			#print("\n")
			return 

		#print("TLPoint", self.TLpoint.iX, ", ", self.TLpoint.iY)
		if ((self.BRpoint.iX + self.TLpoint.iX)/2)>=apoint.iX: #((8-0)/2)>=7 false
			if ((self.BRpoint.iY + self.TLpoint.iY)/2)>=apoint.iY:
				#firstQuadOK
				#print "fq"
				#print("firstQuad", "Point(",apoint.iX,",",apoint.iY,")", "TLPoint(",self.TLpoint.iX,",",self.TLpoint.iY,")","BRPoint(",self.BRpoint.iX,",",self.BRpoint.iY,")")
				#print("(",self.TLpoint.iX,",",self.TLpoint.iY,")(",(self.BRpoint.iX+self.TLpoint.iX)/2,",",(self.BRpoint.iY+self.TLpoint.iY)/2,")")
				if not hasattr(self, 'topLeftChild'):
					self.topLeftChild = quad(self.TLpoint, point((self.BRpoint.iX+self.TLpoint.iX)/2,(self.BRpoint.iY+self.TLpoint.iY)/2),0)
				#print("XYZ",hasattr(self, 'topLeftChild'));
				self.topLeftChild.add(apoint, data)
				#print "Added"
			else:
				#print "tq"
				#thirdQuadOK
				#print("thirdQuad", "Point(",apoint.iX,",",apoint.iY,")", "TLPoint(",self.TLpoint.iX,",",self.TLpoint.iY,")","BRPoint(",self.BRpoint.iX,",",self.BRpoint.iY,")")
				#print(self.TLpoint.iX,",",self.BRpoint.iY/2,"\n")
				if not hasattr(self, 'botLeftChild'):
					self.botLeftChild = quad(point(self.TLpoint.iX,(self.BRpoint.iY+self.TLpoint.iY)/2), point((self.BRpoint.iX+self.TLpoint.iX)/2,self.BRpoint.iY),0)
				#print("(",self.botLeftChild.TLpoint.iX,",",self.botLeftChild.TLpoint.iY,")","(",self.botLeftChild.BRpoint.iX,",",self.botLeftChild.BRpoint.iY,")")
				self.botLeftChild.add(apoint, data)
				#print "Added"
		else:	
			if ((self.BRpoint.iY + self.TLpoint.iY)/2)<apoint.iY:
				#fourthQuadOK
				#print "foq"
				#print("fourthQuad", "Point(",apoint.iX,",",apoint.iY,")", "TLPoint(",self.TLpoint.iX,",",self.TLpoint.iY,")","BRPoint(",self.BRpoint.iX,",",self.BRpoint.iY,")")
				if not hasattr(self, 'botRightChild'):
					self.botRightChild = quad(point((self.BRpoint.iX+self.TLpoint.iX)/2,(self.BRpoint.iY+self.TLpoint.iY)/2), self.BRpoint,0)
				#print("(",(self.BRpoint.iX+self.TLpoint.iX)/2,",",self.TLpoint.iY,")(",self.BRpoint.iX,",",(self.BRpoint.iY+self.TLpoint.iY)/2)
				self.botRightChild.add(apoint, data)
				#print "Added"
			else:
				#secondQuadOK
				#print "sq"
				#print("secondQuad", "Point(",apoint.iX,",",apoint.iY,")", "TLPoint(",self.TLpoint.iX,",",self.TLpoint.iY,")","BRPoint(",self.BRpoint.iX,",",self.BRpoint.iY,")")
				if not hasattr(self, 'topRightChild'):
					self.topRightChild = quad(point((self.BRpoint.iX+self.TLpoint.iX)/2,self.TLpoint.iY), point(self.BRpoint.iX,(self.BRpoint.iY+self.TLpoint.iY)/2),0)
				#print("(",(self.BRpoint.iX),",--,",(self.TLpoint.iX),",",self.TLpoint.iY,")(",self.BRpoint.iX,",",(self.BRpoint.iY+self.TLpoint.iY)/2)
				self.topRightChild.add(apoint, data)
				#print "Added"
		self.iC+=1
		#if(self.iC==3):
			#self.node = node((1,-1,-1), point(-1,-1))

	#to check whether a point is within range of quad or not
	def checkBoundry(self, point):
		#returns true but should false
		#print("if: ",self.TLpoint.iX,"<=",point.iX)
		if self.TLpoint.iX <= point.iX:
			#print("if: ",self.TLpoint.iY,"<=",point.iY)
			if self.TLpoint.iY <= point.iY:
				#print("if: ",self.BRpoint.iX,">=",point.iX) 
				if self.BRpoint.iX >= point.iX:
					#print("if: ",self.BRpoint.iY,">=",point.iY)
					if self.BRpoint.iY >= point.iY:
						return False
		return True

#find nodes at a particular level
def findNodes(q1, flevel, clevel, store):
	if q1==None:
		return
	if clevel==0:
		if hasattr(q1, 'node'):
			store.append(q1.node.data)
		return
	clevel-=1
	if hasattr(q1, 'topLeftChild'):
		findNodes(q1.topLeftChild, flevel, clevel, store)
	if hasattr(q1, 'topRightChild'):
		findNodes(q1.topRightChild, flevel, clevel, store)
	if hasattr(q1, 'botLeftChild'):
		findNodes(q1.botLeftChild, flevel, clevel, store)
	if hasattr(q1, 'botRightChild'):
		findNodes(q1.botRightChild, flevel, clevel, store)		

#find depth of tree
def findDepth(q1, depth):
	tl=tr=bl=br=0
	depth+=1
	if hasattr(q1, 'topLeftChild'):
		tl = findDepth(q1.topLeftChild, depth)
	if hasattr(q1, 'topRightChild'):
		tr = findDepth(q1.topRightChild, depth)
	if hasattr(q1, 'botLeftChild'):
		bl = findDepth(q1.botLeftChild, depth)
	if hasattr(q1, 'botRightChild'):
		br = findDepth(q1.botRightChild, depth)
	return max(tl,tr,bl,br,depth)

def mainFunc(size):
	#make a quad of (0,0) to (width, height)
	height = width = size
	q1 = quad(point(0,0),point(height,width), 0)

	#as image is read in row-by-row, we can generate sequence ((1,1)(2,1)(3,1)...Width) X height 
	seq=list()
	for i in range(1, height+1):
		for j in range(1, width+1):
				seq.append((j, i))
	#print seq
	#make quadtree
	# xyz=[0, 1, 8, 9, 2, 3, 10, 11, 16, 17, 24, 25, 18, 19, 26, 27, 4, 5, 12, 13, 6, 7, 14, 15, 20, 21, 28, 29, 22, 23, 30, 31, 32, 33, 40, 41, 34, 35, 42, 43, 48, 49, 56, 57, 50, 51, 58, 59, 36, 37, 44, 45, 38, 39, 46, 47, 52, 53, 60, 61, 54, 55, 62, 63]
	# xyz=[0, 1, 16, 17, 8, 9, 24, 25, 4, 5, 20, 21, 12, 13, 28, 29, 2, 3, 18, 19, 10, 11, 26, 27, 6, 7, 22, 23, 14, 15, 30, 31, 32, 33, 48, 49, 40, 41, 56, 57, 36, 37, 52, 53, 44, 45, 60, 61, 34, 35, 50, 51, 42, 43, 58, 59, 38, 39, 54, 55, 46, 47, 62, 63]

	myList=list()
	for i in range(0, height*width):
		myList.append(i)

	#print myList
	#2*2-->0Ite
	#4*4-->1Ite
	#8*8-->3Ite
	#16*16-->2Ite
	#32*32-->5Ite
	if(height==2):
		ite=1
		#15Sec
	elif(height==4):
		ite=1
		#15sec
	elif(height==8):
		ite=3
		#45sec
	elif(height==16):
		ite=2
		#30sec
	elif(height==32):
		ite=5
		#75sec 1min-15sec
	elif(height==64):
		ite=9 #1,2,3,5,6,7,8no
		#135sec 2min-15sec
	else:
		print("Only 2,4,8,16,32 length supported yet, there is "+str(height)+" !")
		exit()

	tempList=list()
	# ! 15 SECONDS FOR EACH ITERATION ! #
	for j in range(0, ite):
		for i in range(0, height*width):
			print("Iteration: "+str(i)+"("+str(j+1)+")Total: "+str(ite)+"*"+str(height*width))
			tempList=list()
			q1.add(point(seq[i][0], seq[i][1]), myList[i])
			inorder(q1, tempList)
		
		#print tempList 
		myList=tempList
		#print "asf"

	#print "\n\n"
	print(myList)
	return myList

# counter=0
# for i in range(0, height*width):
# 	#q1.add(point(seq[i][0], seq[i][1]), lists[i])
# 	#print seq[i], counter
# 	q1.add(point(seq[i][0], seq[i][1]), counter)
# 	counter -= -1

# q2level=list()
# inorder(q1, q2level)

# for i in range(0, height*width):
# 	#q1.add(point(seq[i][0], seq[i][1]), lists[i])
# 	#print seq[i], counter
# 	q1.add(point(seq[i][0], seq[i][1]), q2level[i])
# 	#counter -= -1

# q3level=list()
# inorder(q1, q3level)

# for i in range(0, height*width):
# 	q1.add(point(seq[i][0], seq[i][1]), q3level[i])

# myList=list()
# inorder(q1, myList)
# print myList