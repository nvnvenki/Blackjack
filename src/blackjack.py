from random import choice

from deck import Deck
from scorer import Scorer
from player import Player

class Blackjack(object):
	
	def __init__(self):
		super(Blackjack, self).__init__()
		self.deck = Deck()

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

	def play(self):

		# cards may be unlimited - 4 suits in a deck
		start = True
		while start:
			
			player = Player()
			computer = Player()

			player.addCards(self.deck.getCard())
			player.addCards(self.deck.getCard())
		
			if self.__isAllFaceCards(player.getCards()):
				player.setPlayStatus(False)
			
			scorer = Scorer()

			while player.getPlayStatus():
				scorer.addPointsToPlayer(self.__addUpCards(player.getCards()))
				print "Player cards: %s total: %d" % (player.getCards(), scorer.getTotalPlayer())

				if scorer.isBusted('p'):
					print "Player bursted!"
					player.setBurstedStatus(True)
					player.setPlayStatus(False)

				elif scorer.isBlackjack():
					print "Black jack!"
					player.setPlayStatus(False)

				else:
					hit_or_stand = raw_input("hit or stand? h / s : ")
					if hit_or_stand is "h":
						player.addCards(self.deck.getCard())
					else:
						player.setPlayStatus(False)

			while computer.getPlayStatus():
				# almost same
				computer.addCards(self.deck.getCard())
				computer.addCards(self.deck.getCard())

				# till the computer hv 18
				while True:
					scorer.addPointsToComputer(self.__addUpCards(computer.getCards()))
					if scorer.getTotalComputer() <= 18 :
						computer.addCards(self.deck.getCard())
					else:
						break
				print "computer cards: %s total: %d" % (computer.getCards(), scorer.getTotalComputer())

				# who is the winner
				if scorer.getTotalComputer() > 21:
					print "computer bursted!"
					if not player.getBurstedStatus():
						print "player wins!"
					
						
				elif scorer.getTotalComputer() > scorer.getTotalPlayer():
					print "computer wins!"
					

				elif scorer.getTotalComputer() == scorer.getTotalPlayer():
					print "Draw!"

				elif scorer.getTotalPlayer() > scorer.getTotalComputer():
					if not player.getBurstedStatus():
						print "player wins!"

					elif not computer.getBurstedStatus():
						print "computer bursted"

				computer.setPlayStatus(False)
			carryon = raw_input("would you like to continue? y or n : ")
			if carryon is not "y":
				start = False

def main():
	print "-" * 50
	print "A simple two player( player vs computer)"
	print "-" * 50

	game = Blackjack()
	game.play()

if __name__ == '__main__':
	main()