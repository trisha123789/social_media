
from src.dao.echo_dao import EchoDAO

class EchoService:
    dao = EchoDAO()

    @classmethod
    def react(cls, thought_id: int, viber_id: int, emotion: str):
        return cls.dao.react(thought_id, viber_id, emotion)

    @classmethod
    def react_to_post(cls, post_id: int, viber_id: int, emotion: str):
        return cls.dao.react_to_post(post_id, viber_id, emotion)