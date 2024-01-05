import requests
import json

r = requests.get('https://official-joke-api.appspot.com/random_joke')

joke = json.loads(r.text)

print(joke['setup'])
print(">>", joke['punchline'])