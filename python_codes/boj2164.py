sample_cards = [i for i in range(1, int(input()) + 1)]


def babarian(cards:list):
    tmp_cards = cards.copy()
    while True:
        input()
        tmp_cards.pop(0)
        tmp_cards.append(tmp_cards.pop(0))
        print(tmp_cards)
        if len(tmp_cards) == 1:
            break


def advanced(cards:list) -> int:
    while True:

        if len(cards) % 2:
            cards = cards[1::2]
            cards.append(cards[0])
            cards.pop(0)
        else:
            cards = cards[1::2]
        if len(cards) == 1:
            return cards[0]

if len(sample_cards) <= 1:
    print(1)
else:
    print(advanced(sample_cards))
