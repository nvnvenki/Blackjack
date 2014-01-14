from random import shuffle

class Deck(object):
	
	def __init__(self):
		super(Deck, self).__init__()
		cards = [{'Ace' : 11 } ,{'Two' : 2}, {'Three' : 3}, {'Four' : 4},
						{'Five' : 5}, {'Six' : 6}, {'Seven' : 7}, {'Eight' : 8},
						{'Nine' : 9}, {'Ten' : 10}, {'Jack' : 10}, {'King' : 10}, {'Queen' : 10}] 
		suits =  cards * 4

		self.__cards = suits * 4 
		self.__shuffle()

	def __shuffle(self):
		shuffle(self.__cards)

	def getCard(self):
		if len(self.__cards) > 0:
			# self.__shuffle()
			card = self.__cards[0]
			self.__cards = self.__cards[1:]
			# self.__shuffle()
			return card
		else:
			print "No more cards!"
			return None

def main():
	# just testing the code
	deck = Deck()
	print deck.getCard()
	print deck.getCard()
	print deck.getCard()

if __name__ == '__main__':
	main()