from framework.http_petstore_api.put_pet import put_new_pet


def test_add_pet():
    pet_id = 1
    pet_name = 'test_name'
    result = put_new_pet(pet_id, pet_name)
    assert result.status_code == 200
    assert result.json()['id'] == pet_id
    assert result.json()['name'] == pet_name
