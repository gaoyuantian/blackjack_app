import random
def shuffleDeck():
    'return shuffled deck'
    suits={'\u2660','\u2661','\u2662','\u2663'}
    ranks={'A','2','3','4','5','6','7','8','9','10','J','Q','K'}
    deck=[]
    #creat deck of 52 cards
    for suit in suits:
        for rank in ranks:
            deck.append(rank+''+suit)
    #shuffle the deck and return
    random.shuffle(deck)
    return deck

def dealCard(deck,participant):
    'deals single card from deck to participant'
    card=deck.pop()
    participant.append(card)
    return card


def total(hand):
    'returns the value of the blackjack hand'
    'input hand is a list, e.g.[''A''+''\u2660','3''+''\u2661'']'
    values={'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'1':10,'J':10,
            'Q':10,'K':10,'A':11}
    result=0
    numAces=0
    #add up the values of cards in the hand
    for card in hand:
        result+=values[card[0]]
        if card[0]=='A':
            numAces+=1
    while result>21 and numAces>0:
        result-=10
        numAces-=1

    return result

def compareHands(house,player):
    'compare house and player hands and prints outcome'
    houseTotal,playerTotal=total(house),total(player)
    if houseTotal>playerTotal:
        print('you lose.')
    elif houseTotal<playerTotal:
        print('you win')
    elif houseTotal==21 and 2==len(house)<len(player):
        print('you lose')
    elif playerTotal==21 and 2==len(player)<len(house):
        print('you win')
    else:
        print('A tie.')

def blackjack():
    'simulates the house in a game of blackjack'
    deck=shuffleDeck()
    house=[]  #house card: dictionary
    player=[]
    for i in range(2):    #deal the first two cards
        dealCard(deck,player)
        dealCard(deck,house)
    #print hands
    print('House:{:>7}{:>7}'.format(house[0],house[1]))
    print('  You:{:>7}{:>7}'.format(player[0],player[1]))
    # While user requests an additional card, house deals it
    answer=input('Hit or stand?(default:hit):')
    while answer in {'','h','hit'}:
        card = dealCard(deck,player)
        print('You got{:>7}'.format(card))

        if total(player)>21:
              print('You went over...You lose.')
              return
        answer=input('Hit or stand?(default:hit): ')

    # house must play the 'house rules'
    while total(house)<17:
        card=dealCard(deck,house)
        print('House got{:>7}'.format(card))

        if total(house)>21:
            print('House went over...You wins.')
            return
    # compare house and player hands and print results
    compareHands(house,player)



    











