# src/services/soul_link_service.py
from src.dao.soul_link_dao import SoulLinkDAO

class SoulLinkService:
    dao = SoulLinkDAO()

    @classmethod
    def follow(cls, follower_id: int, following_id: int):
        if follower_id == following_id:
            raise ValueError("Cannot follow yourself.")
        # check exists already
        if cls.dao.exists(follower_id, following_id):
            return {"message": "Already following"}
        resp = cls.dao.follow(follower_id, following_id)
        # resp.data holds created record(s) depending on supabase response
        return resp.data

    @classmethod
    def unfollow(cls, follower_id: int, following_id: int):
        if follower_id == following_id:
            raise ValueError("Invalid operation.")
        resp = cls.dao.unfollow(follower_id, following_id)
        return resp.data

    @classmethod
    def get_followers(cls, viber_id: int):
        # returns list of { "follower_id": ..., "created_at": ... }
        return cls.dao.get_followers(viber_id)

    @classmethod
    def get_following(cls, viber_id: int):
        # returns list of { "following_id": ..., "created_at": ... }
        return cls.dao.get_following(viber_id)

    @classmethod
    def is_following(cls, follower_id: int, following_id: int) -> bool:
        return cls.dao.exists(follower_id, following_id)
