class Node(object):
	
	def __init__(self, data=None, next_node=None):
		self.data = data
		self.next_node = next_node

	def get_data(self):
		return self.data

	def get_next(self):
		return self.next_node

	def set_next(self, new_next):
		self.next_node = new_next

class LinkedList(object):

	def __init__(self, head=None):
		self.head = head

	def insert(self,data):
		new_node = Node(data)
		new_node.set_next(self.head)
		self.head = new_node

	def display(self):
		cur = self.head
		elems = []

		while cur != None:
			elems.append(cur.data)
			cur = cur.next_node
			 
		print (elems)

	def delete(self,data):
		cur = self.head
		prev = None
		while cur != None:
			print cur.data
			if cur.data == data:
				prev.next_node = cur.next_node

			prev = cur
			cur = cur.next_node

L = LinkedList()

L.insert(2)
L.insert(3)
L.insert(7)
L.insert(8)
L.insert(0)
L.insert(5)
L.display()
L.delete(8)
L.display()