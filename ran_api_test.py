import pytest
import json, urllib.request


def test_run_api_data():
    with urllib.request.urlopen("http://127.0.0.1:500/") as url:
        result_one = json.loads(url.read().decode())
    with open('./data/data.json', 'r', encoding='utf-8') as file:
        result_two = json.load(file)
        file.close()

    assert result_one == result_two


