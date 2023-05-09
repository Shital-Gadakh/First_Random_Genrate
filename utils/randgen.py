import random


def Produce_characters(start=1, stop=82):
    return (random.randrange(1, stop=82) for item in range(1, 16))
