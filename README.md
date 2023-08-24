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

* Make the number of maximum items configurable so that the webinterface won't
  break
* Configure the number of concurrent events
* Get rid of warnings when starting mongodb
* Should the name of the project be listener?
* Is the setup function in the tests reliable?
* Clean up everything

# Useful Links

https://hub.docker.com/_/mongo
https://www.mongodb.com/languages/python
https://www.mongodb.com/docs/manual/tutorial/expire-data/
https://stackoverflow.com/questions/10938360/how-many-concurrent-requests-does-a-single-flask-process-receive
https://earthly.dev/blog/mongodb-docker/
