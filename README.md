# test_petstore_api
https://petstore.swagger.io

- [x] POST /pet
    - [x] Check added pet for valid request
    - [x] Expected error for request without pet name
    - [x] Expected error for request with invalid value types
    - [x] Expected error for request with invalid status value
- [x] GET /pet/findByStatus
    - [x] Response contains pets only with the requested status
    - [x] Expected empty response for request with invalid status
- [x] GET /pet/{petId}
    - [x] Request with valid petId returns pet
    - [x] Request with nonexistent petId returns status-code 404
    - [x] Expected error for request with invalid petId type
- [x] POST /pet/{petId}
    - [x] Request with existent petId and valid name and status update pet data
    - [x] Error for request with nonexistent petId
    - [x] Error for request with invalid petId
- [x] DELETE /pet/{petId}
    - [x] Request with existent petId remove pet
    - [x] Expected error for request with nonexistent petId
