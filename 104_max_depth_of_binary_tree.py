# A binary tree node
class Node:
 
    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def maxDepth(node):

	if node == None:
		return 0

	ldepth = maxDepth(node.left)
	rdepth = maxDepth(node.right)

	return max(ldepth,rdepth)+1

def minDepth(node):

	if node == None:
		return 0
	if node.left == None and node.right == None:
		return 1
	if node.left == None:
		return minDepth(node.right)+1
	if node.right == None:
		return minDepth(node.left)+1
	return min(minDepth(node.left),minDepth(node.right))+1

def mergeTrees(t1,t2):

	if t1!= None and t2 != None:
		t3 = Node(t1.data+t2.data)
		t3.left = mergeTrees(t1.left,t2.left)
		t3.right = mergeTrees(t1.right,t2.right)
	elif t1 == None and t2 !=None:
		t3 = Node(t2.data)
	elif t1 != None and t2 == None:
		t3 = Node(t1.data)
	else:
		t3 = None
	return t3

def display(root):
		if root != None:
			_display(root)

def _display(node):
	
	if node != None:
		_display(node.left)
		print str(node.data)+ " "
		_display(node.right)


# Driver program to test above function
# root = Node(1)
# root.left = Node(3)
# root.left.left = Node(5)
# root.right = Node(2)

t1 = Node(1)
t1.left = Node(3)
t1.left.left = Node(5)
t1.right = Node(2)

t2 = Node(2)
t2.left = Node(1)
t2.right = Node(3)
t2.left.right = Node(4)
t2.right.right = Node(7)
 
#print "Height of tree is %d" %(maxDepth(root))
#print "Min Height of tree is %d" %(mergeTrees(t1,t2))

t3 = mergeTrees(t1,t2)
display(t3)