from conftest import catfact_api, load_json_schema
from jsonschema.validators import validate


def test_get_facts():
    response = catfact_api(method='get',
                           url='/facts')

    assert response.status_code == 200
    assert len(response.json()['data']) == 10


def test_get_facts_limit():
    limit = 2

    response = catfact_api(method='get',
                           url='/facts',
                           params={'limit': {limit}})

    assert response.status_code == 200
    assert len(response.json()['data']) == limit


def test_get_breeds_schema():
    limit = 6
    schema = load_json_schema('catfacts_get_breeds_schema.json')

    response = catfact_api(
        method='get',
        url='/breeds',
        params={'limit': {limit}}
    )

    validate(instance=response.json(),
             schema=schema)


def test_max_length_fact():
    max_length = 100

    response = catfact_api(method='get',
                           url='/fact',
                           params={"max_length": max_length})

    assert response.json()['length'] <= 100
