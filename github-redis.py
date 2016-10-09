import requests
import redis

db = redis.StrictRedis('localhost', 6379, 0)

url = "https://api.github.com/users/marshyski/repos"

# Get response back in JSON
resp = requests.get(url).json()

langs = []

# Iterate over json array and put language in list
for l in resp:
    if l["language"] != None:
        langs.append(l["language"])

# Get max of highest key in the list of elements
favlang = max(langs, key=langs.count)

# Set value of language
db.set("lang", favlang)

# Set hash timlang with dict
db.hmset("timlang", {"name": "timski", "language": favlang})

# Get value from key lang
print "Favorite language is", db.get("lang")

# Get hash timlang
print db.hgetall("timlang")

# Get hash and value of name
print db.hgetall("timlang")["name"]