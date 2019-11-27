from bjklasy import Card, Hand, Deck

# utworzenie talii
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
