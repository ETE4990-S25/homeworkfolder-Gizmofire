deck = {(s,r) for s in '♥♦♠♣' for r in range(1,14)}
print(deck)

deck2 = {r: {s for s in '♥♦♠♣'} for r in range(1,14)}
print(deck2)