from enum import Enum

class SignalEvent(Event):
	"""
	Created by Strategy objects to give advice on how to trade.
	"""

	def __init__(self, symbol, datetime, signal_type):
		self.type = "SIGNAL"
		self.symbol = symbol
		self.datetime = datetime
		self.signal_type = signal_type
		