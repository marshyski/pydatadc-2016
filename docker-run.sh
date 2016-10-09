#!/bin/bash

docker run -d --net=host --name redis redis
docker run -d --net=host --name elastic elasticsearch
docker run --name kibana --net=host -e ELASTICSEARCH_URL=http://localhost:9200 -d kibana
