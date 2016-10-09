curl "http://localhost:9200/_search?q=title:Marshy%20Ski&size=10&pretty=true"

curl http://localhost:9200/_search -d '{ "query": { "match": { "title": "Marshy Ski" } } }'
