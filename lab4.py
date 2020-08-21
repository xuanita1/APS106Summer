import random
import copy
suits = ['spades', 'clubs', 'diamonds', 'hearts']
def deck():
    """
    () -> lst
    Returns a deck of cards as a list. Each element in the list is a list of a string representing the suit ("spades", "clubs", "diamonds", or "hearts" and an integer representing the number of the card (1 to 13). 
    """
    card_deck=[]
    for suit in suits:
        for number in range(1, 14):
            card_deck.append([suit,number])
    return(card_deck)
def random_shuffle(lst):
    """ 
    (list) -> list
    Receives a list and returns a randomly ordered list containing all of the same elements.
    """
    numbers_list= random.sample(range(52), 52)
    random_card_deck=[]
    for i in numbers_list:
            value = lst[i]
            random_card_deck.append(value)
    return random_card_deck

def reverse(lst):
    """
    (list) -> list
    Receives a list and returns a reverse ordered list containing all of the same elements.
    """
    reverse_card_deck=[]
    for i in range(51,-1,-1):
        value = lst[i]
        reverse_card_deck.append(value)
    return reverse_card_deck
         
    
# Test Code
card_deck_list = deck()
shuffled_deck = random_shuffle(card_deck_list)
reverse_shuffled_card_deck = reverse(shuffled_deck)
print(shuffled_deck)
print(reverse_shuffled_card_deck)

