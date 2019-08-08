class FillEvent(Event):
	"""
	Represents a completed order from a brokerage.
	"""

	def __init__(self, timeindex, symbol, exchange, quantity, direction, fill_cost, commission=None):
		self.type = "FILL"
		self.timeindex = timeindex
		self.symbol = symbol
		self.exchange = exchange
		self.quantity = quantity
		self.direction = direction
		self.fill_cost = fill_cost