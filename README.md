# A Webhook Listener

# Prerequisites

* Docker
* Docker Compose
* Make
* Curl

# How to test

Run the following command and see if everything looks well

    make run

# Todo

* Ensure that the database have automatic retention
* Ensure persistent storage
* Make the number of maximum items configurable
* Configure the number of concurrent events
* Get rid of warnings when starting mongodb
* Should the name of the project be listener?
* End-to-end tests?

# Useful Links
https://hub.docker.com/_/mongo
https://www.mongodb.com/languages/python
https://www.mongodb.com/docs/manual/tutorial/expire-data/
https://stackoverflow.com/questions/10938360/how-many-concurrent-requests-does-a-single-flask-process-receive
