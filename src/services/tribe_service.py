
from src.dao.tribe_dao import TribeDAO

class TribeService:
    dao = TribeDAO()

    @classmethod
    def create(cls, name, description):
        return cls.dao.create(name, description)

    @classmethod
    def list(cls):
        return cls.dao.list()

    @classmethod
    def join(cls, viber_id, tribe_id):
        return cls.dao.join(viber_id, tribe_id)

    @classmethod
    def list_viber_tribes(cls, viber_id):
        return cls.dao.list_viber_tribes(viber_id)




    # New methods
    @classmethod
    def add_resource(cls, tribe_id, viber_id, title, description, url):
        return cls.dao.add_resource(tribe_id, viber_id, title, description, url)

    @classmethod
    def list_resources(cls, tribe_id):
        return cls.dao.list_resources(tribe_id)

    @classmethod
    def list_members(cls, tribe_id):
        return cls.dao.list_members(tribe_id)
