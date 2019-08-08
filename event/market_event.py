class MarketEvent(Event):
	"""
	Signifies change in market state.
	"""

	def __init__(self):
		self.type = "MARKET"
