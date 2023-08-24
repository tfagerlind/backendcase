#!/bin/sh

curl -X POST localhost:5000 -H 'Content-Type: application/json' -d @producer/event1.json
curl -X POST localhost:5000 -H 'Content-Type: application/json' -d @producer/event2.json
