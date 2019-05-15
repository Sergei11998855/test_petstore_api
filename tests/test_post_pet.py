from framework.http_petstore_api.post_pet import PostPet


class TestPostPet:

    def test_add_pet_with_valid_data(self):
        pet_id = 1
        pet_name = 'valid_pet_name'
        result = PostPet().add_new_pet(pet_id, pet_name)
        assert result.status_code == 200, f'Expected status-code 200, not {result.status_code}'
        assert result.json()['id'] == pet_id, f'pet_id not equal {pet_id}'
        assert result.json()['name'] == pet_name, f'pet_name not equal {pet_name}'

    def test_request_without_pet_name(self):
        pet_id = 1
        pet_name = None
        result = PostPet().add_new_pet(pet_id, pet_name)
        assert result.status_code == 405, \
            f'Expected status-code 405, not {result.status_code}, pet name is required field'

    def test_request_with_invalid_value_types(self):
        pet_id = 'string instead int'
        result = PostPet().add_new_pet(pet_id)
        assert result.status_code == 500, \
            f'Expected status-code 500, not {result.status_code}, request contains invalid pet id'

    def test_request_with_invalid_status_value(self):
        invalid_status = 'invalid_status_value'
        result = PostPet().add_new_pet(status=invalid_status)
        assert result.status_code == 405, \
            f'Expected status-code 405, not {result.status_code}, request contains invalid status'
