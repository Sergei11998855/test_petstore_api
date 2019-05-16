import requests

url = 'https://petstore.swagger.io/v2'
headers_json = {'Content-Type': 'application/json'}
headers_x_form = {'Content-Type': 'application/x-www-form-urlencoded'}

def find_pet_by_id(pet_id):
    return requests.get(url=f'{url}/pet/{pet_id}', headers=headers_json)


def post_pet(request_json):
    return requests.post(url=f'{url}/pet', json=request_json, headers=headers_json)


def put_pet(request_json):
    return requests.put(url=f'{url}/pet', json=request_json, headers=headers_json)


def get_find_by_status(status):
    return requests.get(url=f'{url}/pet/findByStatus?status={status}', headers=headers_json)


def post_update_pet_by_id(pet_id, name, status):
    request_json = {'name': name, 'status': status}
    return requests.post(url=f'{url}/pet/{pet_id}', data=request_json, headers=headers_x_form)
