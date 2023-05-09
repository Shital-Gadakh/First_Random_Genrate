from utils.randgen import Produce_characters

start = 1
stop = 15
obj = Produce_characters()
for i in range(start, stop + 1):
    print(next(obj))

# For run Command(python swapi_01.py)
