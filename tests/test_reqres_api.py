from jsonschema.validators import validate
from conftest import load_json_schema, reqres_api
import allure


@allure.description('Get users list per page')
def test_get_users_list_per_page():
    per_page = 6
    response = reqres_api(method='get',
                          url='/api/users',
                          params={'per_page': per_page})

    assert response.status_code == 200
    assert response.json()['per_page'] == per_page
    assert len(response.json()['data']) == per_page


@allure.description('Get single user data')
def test_get_found_single_user_data():
    id = 2
    response = reqres_api(method='get',
                          url='/api/users',
                          params={'id': id})

    assert response.status_code == 200
    assert response.json()['data']['id'] == id


@allure.description('Not found user data status code')
def test_get_single_user_not_found_status_code():
    id = 77
    response = reqres_api(method='get',
                          url='/api/users',
                          params={'id': id})

    assert response.status_code == 404


@allure.description('Validate json response for get users list')
def test_get_users_list_response_format():
    schema = load_json_schema('get_users_list_schema.json')

    response = reqres_api(method='get',
                          url='/api/users')

    validate(instance=response.json(),
             schema=schema)


@allure.description('Validate json response for create user')
def test_create_user_response_format():
    schema = load_json_schema('create_new_user_response_schema.json')

    payload = {
        "name": "morpheus01",
        "job": "leader"
    }
    response = reqres_api(method='post',
                          url='/api/users',
                          json=payload)

    assert response.status_code == 201
    validate(instance=response.json(),
             schema=schema)
    assert response.json()['name'] == payload['name']
    assert response.json()['job'] == payload['job']


@allure.description('Validate json response for register user')
def test_successful_register_user_response_format():
    schema = load_json_schema('successful_register_schema.json')

    payload = {
        "email": "eve.holt@reqres.in",
        "password": "pistol"
    }

    response = reqres_api(method='post',
                          url='/api/register',
                          json=payload)

    assert response.status_code == 200
    validate(instance=response.json(),
             schema=schema)


@allure.description('Register user with empty data status code')
def test_register_user_empty_data_status_code():
    payload = {
        "email": "",
        "password": ""
    }
    response = reqres_api(method='post',
                          url='/api/register',
                          json=payload)

    assert response.status_code == 400


@allure.description('Delete user status code')
def test_delete_user_status_code():
    response = reqres_api(method='delete',
                          url='/api/users/2')

    assert response.status_code == 204


@allure.description('Validate json response for get single resource')
def test_get_single_resource_response_format():
    schema = load_json_schema('get_single_resource_schema.json')

    response = reqres_api(method='get',
                          url='/api/unknown/2')

    assert response.status_code == 200
    validate(instance=response.json(),
             schema=schema)


@allure.description('Validate json response for update user data')
def test_update_single_user_format_json():
    schema = load_json_schema('update_single_user_response_schema.json')

    payload = {
        "name": "morpheus",
        "job": "zion resident"
    }

    response = reqres_api(method='put',
                          url='/api/users/2',
                          json=payload)

    assert response.status_code == 200
    validate(response.json(), schema=schema)
    assert response.json()['name'] == payload['name']
    assert response.json()['job'] == payload['job']
