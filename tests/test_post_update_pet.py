from framework.http_petstore_api.http_petstore_api import post_update_pet_by_id, find_pet_by_id


class TestPostUpdatePet:

    def test_update_pet_by_id(self):
        pet_id = 1
        name = 'valid name'
        status = 'test status'
        response = post_update_pet_by_id(pet_id, name, status)
        assert response.status_code == 200, f'Expected status-code 200, not {response.status_code}'
        pet = find_pet_by_id(pet_id).json()
        assert pet['id'] == 1, f'pet_id not equal {pet_id}'
        assert pet['name'] == name, f'status not equal {name}'
        assert pet['status'] == status, f'status not equal {status}'

    def test_check_response_with_nonexistent_pet_id(self):
        nonexistent_pet_id = 9999999999
        name = 'valid name'
        status = 'test status'
        response = post_update_pet_by_id(nonexistent_pet_id, name, status)
        assert response.status_code == 404, f'Expected status-code 404, not {response.status_code}'

    def test_check_response_with_invalid_type_pet_id(self):
        invalid_pet_id = 'not string'
        name = 'valid name'
        status = 'test status'
        response = post_update_pet_by_id(invalid_pet_id, name, status)
        assert response.status_code == 400, f'Expected status-code 400, not {response.status_code}'
