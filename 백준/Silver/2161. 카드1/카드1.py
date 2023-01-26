pop_card = []
num = int(input())
card = list(range(1, num+1))

while len(card) > 1:
    pop_card.append(card[0])
    card.pop(0)
    
    card.append(card.pop(0))


print(*pop_card, *card)