import random

def coin_flip():
    """Randomly return 'heads' or 'tails'."""
    if random.randint(0, 1) == 0:
        return "heads"
    else:
        return "tails"

def unfair_coin_flip(probability_of_tails):
    """Randomly (unfair) return 'heads' or 'tails'."""
    if random.random() < probability_of_tails:
        return "tails"
    else:
        return "heads"


# First initialize the tallies to 0
heads_tally = 0
tails_tally = 0

for trial in range(10_000):
    if unfair_coin_flip(0.9) == "heads":
        heads_tally = heads_tally + 1
    else:
        tails_tally = tails_tally + 1

ratio = heads_tally / tails_tally
print(f"The ratio of heads to tails is {ratio}")
