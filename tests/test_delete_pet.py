from framework.http_petstore_api.http_petstore_api import delete_pet, get_find_pet_by_id, post_pet
from framework.http_petstore_api.post_pet import PostPet


class TestDeletePet:

    def test_delete_pet_id(self):
        pet_id = 1
        PostPet().add_new_pet(pet_id)
        response = delete_pet(pet_id)
        assert response.status_code == 200, f'Expected status-code 200, not {response.status_code}'
        deleted_pet = get_find_pet_by_id(pet_id)
        assert deleted_pet.status_code == 404, f'Pet with id={pet_id} is deleted, expected status-code 404'

    def test_check_request_with_nonexistent_pet_id(self):
        nonexistent_pet_id = 9999999999
        response = delete_pet(nonexistent_pet_id)
        assert response.status_code == 404, f'Expected status-code 404, not {response.status_code}'
