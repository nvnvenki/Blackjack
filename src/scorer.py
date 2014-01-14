
class Scorer(object):
	def __init__(self, player):
		super(Scorer, self).__init__()
		self.player = player
	
	def __getTotal(self, cards):
		total = 0
		for eachCard in cards:
			total = total + eachCard[eachCard.keys()[0]]
		return total
	
	def __addUpCards(self, cards):
		number_of_aces = cards.count({'Ace' : 11}) # check the number of aces that the player is having
		total = self.__getTotal(cards) 

		# aces value?? 1 or 11! - decision taken here also make sure that the total is maximized
		if total > 21 and number_of_aces > 0:
			while number_of_aces > 0 and total > 21:
				total = total - 10
				number_of_aces = number_of_aces - 1
		return total

	def __isAllFaceCards(self, cards):
		return len(cards) == 2 and (cards[0].values()[0] == 10 and cards[1].values()[0] == 10)



		