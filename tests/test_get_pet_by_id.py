from framework.http_petstore_api.http_petstore_api import find_pet_by_id


def test_find_pet_by_id():
    pet_id = 1
    pet = find_pet_by_id(pet_id)
    assert pet.json()['id'] == pet_id

