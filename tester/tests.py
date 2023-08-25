"""Functional test suite of webhook service."""
# pylint: disable=missing-function-docstring,redefined-outer-name
# pylint: disable=unused-argument
from http import HTTPStatus
import json
import pytest
import requests


def html_to_json(code):
    """Strip HTML elements that surrounds the JSON code."""
    return json.loads(code.lstrip('<pre>').rstrip('</pre>'))


@pytest.fixture
def setup():
    requests.post('http://listener/clear', timeout=10)


def test_database_is_empty_initially(setup):
    response = requests.get('http://listener', timeout=10)

    assert response.status_code == HTTPStatus.OK
    assert html_to_json(response.text) == []


def test_events_can_be_retrieved(setup):
    data = {'foo': 'bar'}
    requests.post('http://listener/event', json=data, timeout=10)
    get_response = requests.get('http://listener', timeout=10)

    assert get_response.status_code == HTTPStatus.OK
    assert html_to_json(get_response.text) == [data]


def test_events_can_be_cleared(setup):
    event = {'foo': 'bar'}
    requests.post('http://listener/event', json=event, timeout=10)
    requests.post('http://listener/clear', timeout=10)
    get_response = requests.get('http://listener', timeout=10)

    assert get_response.status_code == HTTPStatus.OK
    assert html_to_json(get_response.text) == []
