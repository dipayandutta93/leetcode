# A binary tree node
class Node:
 
    # Constructor to create a new node
    def __init__(self, val):
        self.val = val
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

	if t1 == None and t2 == None:
		return None	
	if t1:
		val1, l1, r1 = t1.val, t1.left, t1.right
	else:
		val1, l1, r1 = 0, None, None
	if t2:
		val2, l2, r2 = t2.val, t2.left, t2.right
	else:
		val2, l2, r2 = 0, None, None
	print val1
	t3 = Node(val1+val2)
	t3.left = mergeTrees(l1,l2)
	t3.right = mergeTrees(r1,r2)
	return t3

def findSecondMinimumValue(root):

	if root == None or root.left == None or root.right == None:
		return -1
	elif root.left == root.right:
		return max(findSecondMinimumValue(root.left,root.right))
	else:
		return max(root.left,root.right)

def display(root):
		if root != None:
			_display(root)

def _display(node):
	
	if node != None:
		_display(node.left)
		print str(node.val)+ " "
		_display(node.right)


# Driver program to test above function
# root = Node(1)
# root.left = Node(3)
# root.left.left = Node(5)
# root.right = Node(2)

t1 = Node(2)
t1.left = Node(2)
t1.right= Node(5)
t1.right.left = Node(5)
t1.right.right = Node(7)

t2 = Node(1)
#t2.left = Node(1)
t2.right = Node(2)
#t2.left.right = Node(4)
t2.right.right = Node(3)
 
#print "Height of tree is %d" %(maxDepth(root))
#print "Min Height of tree is %d" %(mergeTrees(t1,t2))

#t3 = mergeTrees(t1,t2)
#print t3
#display(t3)
print "findSecondMinimumValue: %d"%findSecondMinimumValue(t1)