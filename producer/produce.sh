set -x

sleep 5
curl -X POST listener:8090 -d @/app/event1.json
curl -X POST listener:8090 -d @/app/event2.json
