class ListNode:
	def __init__(self, data=None, next=None):
		self.data = data
		self.next = next

	def set_data(self, data):
		self.data = data

	def get_data(self):
		return self.data

	def set_next(self, next):
		self.next = next

	def get_next(self):
		return self.next

	def has_next(self):
		return self.next != None

	def __repr__(self):
		return '{{data: {!r}, next: {!r}}}'.format(self.data, self.next)

class LinkedList:
	def __init__(self):
		self.head = ListNode()

	def insert(self, node):
		try:
			node.set_next(self.head.get_next())
			self.head.set_next(node)
		except AttributeError as err:
			raise RuntimeError('insert a list node') from err

	def __repr__(self):
		data = []
		next_node = self.head
		while next_node:
			data.append(str(next_node.get_data()))
			next_node = next_node.get_next()
		return '-->'.join(data)


if __name__ == '__main__':
	linked_list = LinkedList()
	linked_list.insert(ListNode(1))
	linked_list.insert(ListNode('hello'))
	linked_list.insert(ListNode('hi'))
	print(linked_list)



