import requests

url = 'https://petstore.swagger.io/v2'
headers = {'Content-Type': 'application/json'}


def find_pet_by_id(pet_id):
    return requests.get(url=f"{url}/pet/{pet_id}", headers=headers)


def post_pet(request_json):
    return requests.post(url=f'{url}/pet', json=request_json, headers=headers)


def put_pet(request_json):
    return requests.put(url=f'{url}/pet', json=request_json, headers=headers)


def get_find_by_status(status):
    return requests.get(url=f"{url}/pet/findByStatus?status={status}", headers=headers)

