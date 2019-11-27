from bjklasy import Card, Hand, Deck

# utworzenie talii - talia o nazwie deck1
deck1 = Deck()
print("Utworzono nową talię.")
print("Talia:")
print(deck1)

# dodanie kompletu kart do talii
deck1.populate()
print("\nDodałem do talii komplet kart.")
print("Talia:")
print(deck1)

# tasowanie kart
deck1.shuffle()
print("\nPotasowałem talię kart.")
print("Talia:")
print(deck1)

# tworzenie ręki gracza i ręki komputera
my_hand = Hand()
your_hand = Hand()
hands = [my_hand, your_hand]

# rozdanie kart do ręki
deck1.deal(hands, per_hand = 5)

# wyświetlanie wyniki rozdania czyli ręce i talię
print("\nRozdałem sobie i Tobie po 5 kart.")
print("Moja ręka:")
print(my_hand)
print("Twoja ręka:")
print(your_hand)
print("Talia:")
print(deck1)
deck1.clear()
print("\nUsunąłem zawartość talii.")
print("Talia:", deck1)
input("\n\nAby zakończyć program, naciśnij klawisz Enter.")
