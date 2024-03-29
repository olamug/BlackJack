from bjklasy import Card, Hand

card1 = Card(rank='A', suit='c')
print('Wyświetlam obiekt karty (klasy Card):')
print(card1)
# część główna
card1 = Card(rank='A', suit='c')

print('Wyświetlam obiekt karty (klasy Card):')
print(card1)
card2 = Card(rank='2', suit='c')
card3 = Card(rank='3', suit='c')
card4 = Card(rank='4', suit='c')
card5 = Card(rank='5', suit='c')

print('\nWyświetlam resztę obiektów po jednym na raz:')
print(card2)
print(card3)
print(card4)
print(card5)

my_hand = Hand()
print('\nWyświetlam zawartość mojej ręki przed dodaniem jakichkolwiek kart:')
print(my_hand)

my_hand.add(card1)
my_hand.add(card2)
my_hand.add(card3)
my_hand.add(card4)
my_hand.add(card5)
print('\nWyświetlam zawartość mojej ręki po dodaniu 5 kart:')
print(my_hand)
your_hand = Hand()
my_hand.give(card1, your_hand)
my_hand.give(card2, your_hand)
print("\nPrzekazuję pierwsze dwie karty z mojej ręki do Twojej.")
print("----------------------------------")
print("Twoja ręka:")
print(your_hand)
print("Moja ręka:")
print(my_hand)

my_hand.clear()
print("\nMoja ręka po usunięciu z niej kart:")
print(my_hand)
input("\n\nAby zakończyć program, naciśnij klawisz Enter.")

