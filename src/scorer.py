class Scorer(object):
	def __init__(self):
		super(Scorer, self).__init__()
		self.total_player = 0
		self.total_computer = 0
	
	def addPointsToPlayer(self, points):
		self.total_player = points

	def addPointsToComputer(self, points):
		self.total_computer = points

	def isBusted(self, who):
		if who is "c":
			if self.total_computer > 21:
				return True
			else:
				return False

		elif who is "p":
			if self.total_player > 21:
				return True
			else:
				return False

	def isBlackjack(self):
		return self.total_player == 21

	def getTotalComputer(self):
		return self.total_computer

	def getTotalPlayer(self):
		return self.total_player





		