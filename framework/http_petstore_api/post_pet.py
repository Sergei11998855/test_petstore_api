from framework.http_petstore_api.http_petstore_api import post_pet


class PostPet:

    def add_new_pet(self, pet_id=1, pet_name='test_pet_name', status='available'):
        category = self._category()
        tags = self._tags()
        request = {'id': pet_id,
                   'category': category,
                   'name': pet_name,
                   'tags': [tags],
                   'status': status}
        return post_pet(request)

    @staticmethod
    def _tags(tag_id=1, name='test'):
        tags = {'id': tag_id,
                'name': name}
        return tags

    @staticmethod
    def _category(category_id=1, name='test'):
        category = {'id': category_id,
                    'name': name}
        return category
