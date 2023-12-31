# Backend Case

This project consists in a webhook listener service, that stores webhook events.
The service also provides a web page that displays all events.

# Prerequisites

* Docker
* Docker Compose
* Make
* Curl

# How to test and run syntax checks

    make test
    make lint

# How to run

First of all start the service with the following command

    make run

When the service is up and running the the service is listening to post events
on on port `localhost:80/webhook`. All events are displayed by the web page on
`localhost:80`.

In order to manually test the the service, fake events can now be sent to the
service by running

    make produce

The content of the database can be cleared by running

    make clear

## Debugging

To facilitate debugging, instead of running `make run` the following command can
be used:

    make debug

A Mongo Express service is now started at `localhost:8081` that can be used to
get more information from the database.
