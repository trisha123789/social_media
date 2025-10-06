from src.dao.reverberation_dao import ReverberationDAO

class ReverberationService:
    dao = ReverberationDAO()

    @classmethod
    def create(cls, thought_id: int = None, post_id: int = None, viber_id: int = None, content: str = ""):
        # allow creating for thought or post
        return cls.dao.create(thought_id=thought_id, post_id=post_id, viber_id=viber_id, content=content)

    @classmethod
    def list(cls, thought_id: int):
        # list comments for a thought
        return cls.dao.list_by_thought(thought_id)


    @staticmethod
    def list_all():
        # fetch all reverberations
        return ReverberationService.dao.list_all()
    
    @staticmethod
    def list_post(post_id):
        return [c for c in ReverberationService.list_all() if c.get("post_id") == post_id]


    @classmethod
    def list_post(cls, post_id: int):
        return cls.dao.list_by_post(post_id)

    @classmethod
    def create_post_comment(cls, post_id: int, viber_id: int, content: str):
        return cls.dao.create_post_comment(post_id, viber_id, content)
