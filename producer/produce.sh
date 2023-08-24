#!/bin/sh

sleep 5
curl -X POST listener:5000 -H 'Content-Type: application/json' -d @/app/event1.json
curl -X POST listener:5000 -H 'Content-Type: application/json' -d @/app/event2.json
