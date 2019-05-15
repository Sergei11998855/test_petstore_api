from framework.http_petstore_api.post_pet import PostPet


class TestPostPet:

    def test_add_pet_with_valid_data(self):
        pet_id = 1
        pet_name = 'valid_pet_name'
        response = PostPet().add_new_pet(pet_id, pet_name)
        assert response.status_code == 200, f'Expected status-code 200, not {response.status_code}'
        pet = response.json()
        assert pet['id'] == pet_id, f'pet_id not equal {pet_id}'
        assert pet['name'] == pet_name, f'pet_name not equal {pet_name}'

    def test_request_without_pet_name(self):
        pet_id = 1
        pet_name = None
        response = PostPet().add_new_pet(pet_id, pet_name)
        assert response.status_code == 400, \
            f'Expected status-code 400, not {response.status_code}, pet name is required field'

    def test_request_with_invalid_value_types(self):
        pet_id = 'string instead int'
        response = PostPet().add_new_pet(pet_id)
        assert response.status_code == 500, \
            f'Expected status-code 500, not {response.status_code}, request contains invalid pet id'

    def test_request_with_invalid_status_value(self):
        invalid_status = 'invalid_status_value'
        response = PostPet().add_new_pet(status=invalid_status)
        assert response.status_code == 400, \
            f'Expected status-code 400, not {response.status_code}, request contains invalid status'
