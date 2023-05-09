from utils.randgen import Produce_characters

start = 1
stop = 15

obj = Produce_characters()
characters = []

for i in range(start, stop + 1):
    characters.append(next(obj))

if __name__ == "__main__":
    print(__name__)
    print("Current module getting excute")

    home_url = "https://swapi.dev"
    relative = "/api/people/{0}"

    for num_ in characters:
        absolute_url = home_url + relative.format(num_)
        print(absolute_url)

# For run Command(python swapi_starwar_01.py)



# __main__
# Current module getting excute
# https://swapi.dev/api/people/32
# https://swapi.dev/api/people/58
# https://swapi.dev/api/people/37
# https://swapi.dev/api/people/7
# https://swapi.dev/api/people/71
# https://swapi.dev/api/people/57
# https://swapi.dev/api/people/61
# https://swapi.dev/api/people/46
# https://swapi.dev/api/people/9
# https://swapi.dev/api/people/45
# https://swapi.dev/api/people/1
# https://swapi.dev/api/people/13
# https://swapi.dev/api/people/69
# https://swapi.dev/api/people/51
# https://swapi.dev/api/people/71