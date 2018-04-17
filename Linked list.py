#Ellene Gay S. Daniel
#Linked List

class Node :
	def __init__( self, data ) :
		self.data = data
		self.next = None
		self.prev = None

class Linked_List :
	def __init__( self ) :
		self.head = None

	def add( self, data ) :
		node = Node( data )
		if self.head == None :
			self.head = node
		else :
			node.next = self.head
			node.next.prev = node
			self.head = node

	def search( self, x ) :
		y = self.head
		if y != None :
			while y.next != None :
				if ( y.data == x ) :
					return y
				y = y.next
			if ( y.data == x ) :
				return y
		return None

	def remove( self, y ) :
		tmp = y.prev
		y.prev.next = y.next
		y.prev = tmp

	def __str__( self ) :
		z = " "
		y = self.head
		if y != None :
			while y.next != None :
				z += y.data
				y = y.next
			z += y.data
		return z


w = Linked_List()

w.add( "Ellene  " ), w.add( "kawawang " ), w.add( "Naiwan ako sa swimming  " ), w.add( "Hi, " )
print (w)

w.remove( w.search( "kawawang " ) )
print (w)
