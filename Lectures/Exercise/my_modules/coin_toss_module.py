import random

def coin_toss(heads_prob=0.5):
    '''Return "heads" or "tails" with a specified probability'''
    x = random.random()
    if x < heads_prob:
        return "heads"
    else:
        return "tails"

