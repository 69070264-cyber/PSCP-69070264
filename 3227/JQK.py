"""Card Name Converter"""

card = input().strip().upper()

suit_code = card[-1]
rank_code = card[:-1]

rank_names = {
    "A": "ace",
    "J": "jack",
    "Q": "queen",
    "K": "king"
}

suit_names = {
    "D": "diamonds",
    "H": "hearts",
    "S": "spades",
    "C": "clubs"
}

rank = rank_names.get(rank_code, rank_code)
suit = suit_names.get(suit_code, suit_code)

print(f"{rank} of {suit}")
