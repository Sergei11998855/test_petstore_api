from framework.http_petstore_api.models import Pet, Category, Tag
from framework.http_petstore_api.http_petstore_api import put_pet


def put_new_pet(pet_id, pet_name):
    category = Category(id=1, name='test')
    photo_urls = ['/test_url/1', '/test_url/2']
    tags = Tag(id=1, name='test')
    request = Pet(id=pet_id,
                  category=category,
                  name=pet_name,
                  photo_urls=photo_urls,
                  tags=[tags], status='available').to_struct()
    return put_pet(request)
