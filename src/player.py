class Player(object):
	"""docstring for Player"""
	def __init__(self):
		super(Player, self).__init__()
		self.bursted = False
		self.play = True
		self.cards = []

	def setBurstedStatus(self, status):
		self.bursted = status

	def getBurstedStatus(self):
		return self.bursted

	def setPlayStatus(self, status):
		self.play = status

	def getPlayStatus(self):
		return self.play

	def addCards(self, card):
		self.cards.append(card)

	def getCards(self):
		return self.cards
		