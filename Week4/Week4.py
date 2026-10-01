from random import choice
coin = choice(["heads", "tails"])
print(coin)

import random
number = random.randint(1, 10)
print(number)
cards = ["jack", "queen", "king"]
random.shuffle(cards)

for card in cards:
    print(card)

import statistics
print(statistics.mean([100,90]))

import cowsay
cowsay.cow("Hello")

import json
import requests
import sys
response = requests.get(
    "https://itunes.apple.com/search?entity=song&limit=5&term=" + sys.argv[1])
o = response.json()
for result in o["results"]:
    print(result["trackName"])


for i in sys.argv[1:]:
    print("My name is", i)

if len(sys.argv) < 2:
    sys.exit("Too few arguments")
elif len(sys.argv) == 2:
    sys.exit("my name is " + sys.argv[1])
else:
    sys.exit("Too many arguments")

