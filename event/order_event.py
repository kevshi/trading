class OrderEvent(Event):
	"""
	Signifies event to execute order on stock.
	"""

	def __init__(self, symbol, order_type, quantity, direction):
		self.type = "ORDER"
		self.symbol = symbol
		self.order_type = order_type
		self.quantity = quantity
		self.direction = direction
		