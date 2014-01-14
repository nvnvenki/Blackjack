from random import choice

from deck import Deck
from scorer import Scorer

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
			
			player_cards = []
			player_cards.append(self.deck.getCard())
			player_cards.append(self.deck.getCard())


			player_bursted = False
			computer_bursted = False

			# palyers turn
			player_play = True
			if self.__isAllFaceCards(player_cards):
				player_play = False
			
			scorer = Scorer()

			while player_play:
				scorer.addPointsToPlayer(self.__addUpCards(player_cards))
				print "Player cards: %s total: %d" % (player_cards, scorer.getTotalPlayer())

				if scorer.isBusted('p'):
					print "Player bursted!"
					player_bursted = True
					player_play = False

				elif scorer.isBlackjack():
					print "Black jack!"
					player_play = False

				else:
					hit_or_stand = raw_input("hit or stand? h / s : ")
					if hit_or_stand is "h":
						player_cards.append(self.deck.getCard())
					else:
						player_play = False

			computer_play = True

			while computer_play:
				# almost same
				computer_cards = []
				computer_cards.append(self.deck.getCard())
				computer_cards.append(self.deck.getCard())

				# till the computer hv 18
				while True:
					scorer.addPointsToComputer(self.__addUpCards(computer_cards))
					if scorer.getTotalComputer() <= 18 :
						computer_cards.append(choice(computer_cards))
					else:
						break
				print "computer cards: %s total: %d" % (computer_cards, scorer.getTotalComputer())

				# who is the winner
				if scorer.getTotalComputer() > 21:
					print "computer bursted!"
					if not player_bursted:
						print "player wins!"
					
						
				elif scorer.getTotalComputer() > scorer.getTotalPlayer():
					print "computer wins!"
					

				elif scorer.getTotalComputer() == scorer.getTotalPlayer():
					print "Draw!"

				elif scorer.getTotalPlayer() > scorer.getTotalComputer():
					if not player_bursted:
						print "player wins!"

					elif not computer_bursted:
						print "computer bursted"

				computer_play = False
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