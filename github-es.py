import requests
import elasticsearch
import json
import os
from requests.auth import HTTPBasicAuth

# Connect to ElasticSearch
es = elasticsearch.Elasticsearch("127.0.0.1", port=9200)

# Delete & Create index
es.indices.delete(index="github", ignore=[400, 404])
es.indices.create(index="github", ignore=400)

token = os.environ['TOKEN']

url = "https://api.github.com/search/users?q=tim"

# Get a response of searched users named Tim
resp = requests.get(url, auth=HTTPBasicAuth("marshyski", token)).json()["items"]

people = []

# Create a list of people from response
for p in resp:
    people.append(p["login"])

# Iterate over people list
for p in people:
    url = "https://api.github.com/users/" + p + "/repos"
    resp = requests.get(url, auth=HTTPBasicAuth("marshyski", token)).json()
    langs = []

    # Iterate over json array and put language in list
    for l in resp:
        if l["language"] != None:
            langs.append(l["language"])

    # Get favorite language
    favlang = max(langs, key=langs.count)
    person = {}
    person["name"] = p
    person["language"] = favlang
    data = json.dumps(person)

    # POST to ElasticSearch
    res = es.index(index="github", doc_type="people", id=p, body=data)
    print "Created", res['created'], "\n"