from framework.http_petstore_api.http_petstore_api import get_find_pet_by_id


class TestFindPetById:

    def test_find_pet_by_id(self):
        pet_id = 1
        response = get_find_pet_by_id(pet_id)
        pet = response.json()
        assert response.status_code == 200
        assert pet['id'] == pet_id, f'Expected pet with id {pet_id}, not {pet["id"]}'

    def test_request_with_invalid_pet_id_type(self):
        invalid_id_type = 'string_id'
        response = get_find_pet_by_id(invalid_id_type)
        assert response.status_code == 400, f'Expected status-code {400}, not {response.status_code}'

    def test_request_with_nonexistent_pet_id(self):
        nonexistent_pet_id = 9999999999
        response = get_find_pet_by_id(nonexistent_pet_id)
        assert response.status_code == 404, f'Expected status-code {404}, not {response.status_code}'
