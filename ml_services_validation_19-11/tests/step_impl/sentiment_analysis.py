import os

import requests
from getgauge.python import continue_on_failure, data_store, step

URL = os.environ["API_URL"] + "/analyze/"


@step("Request sentiment analysis with text <text> returns <status_code>")
def assert_response_code(text, status_code):
    params = {}
    if text:
        params["text"] = text

    with requests.get(URL, params=params) as response:
        assert response.status_code == int(status_code)

    data_store.scenario["response"] = response.json()


@step("Response schema contains attributes <table>")
def assert_response_schema(table):
    response = data_store.scenario["response"]

    for attribute in table.get_column_values_with_name("Attribute"):
        assert attribute in response


@continue_on_failure
@step("Analyze and validate the following texts <table>")
def assert_words_vowel_count(table):
    fails = set()

    for i, row in enumerate(table):
        with requests.get(URL, params={"text": row[1]}) as response:
            data = response.json()

            if row[0] == data["sentiment"]:
                fails.add(i)

    assert not fails, fails
