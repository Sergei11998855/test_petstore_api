import pytest
from framework.http_petstore_api.http_petstore_api import get_find_by_status


class TestGetFindByStatus:
    statuses = ['available', 'pending', 'sold']

    @pytest.mark.parametrize('status', statuses)
    def test_response_contains_only_requested_status(self, status):
        response = get_find_by_status(status)
        for pet in response.json():
            assert pet['status'] == status, f'Expected status: {status} instead {pet["status"]}'

    def test_request_with_invalid_status(self):
        invalid_status = 'invalid'
        response = get_find_by_status(invalid_status)
        assert response.json() == [], 'Expected empty response'
