import requests
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
        print(f"fetching deatils using - {absolute_url} =>\n")
        response = requests.get(absolute_url)
        response = response.json()
        print(response)
        print("########" * 25)

# For run Command(python swapi_starwar_01.py)
