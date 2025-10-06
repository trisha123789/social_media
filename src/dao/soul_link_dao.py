# src/dao/soul_link_dao.py
from src.config import get_supabase

class SoulLinkDAO:
    """
    DAO for soul_links (followers/following) table.
    Schema assumed:
      - link_id SERIAL PRIMARY KEY
      - follower_id INT references vibers(viber_id)
      - following_id INT references vibers(viber_id)
      - created_at timestamptz default now()
      - UNIQUE(follower_id, following_id)
    """

    def __init__(self):
        self._db = get_supabase()

    def follow(self, follower_id: int, following_id: int):
        # Prevent following yourself at DB layer as well (we'll check in service too)
        return self._db.table("soul_links").insert({
            "follower_id": follower_id,
            "following_id": following_id
        }).execute()

    def unfollow(self, follower_id: int, following_id: int):
        return self._db.table("soul_links") \
            .delete() \
            .eq("follower_id", follower_id) \
            .eq("following_id", following_id) \
            .execute()

    def get_followers(self, viber_id: int):
        # returns rows where following_id == viber_id
        resp = self._db.table("soul_links").select("follower_id, created_at").eq("following_id", viber_id).execute()
        return resp.data or []

    def get_following(self, viber_id: int):
        # returns rows where follower_id == viber_id
        resp = self._db.table("soul_links").select("following_id, created_at").eq("follower_id", viber_id).execute()
        return resp.data or []

    def exists(self, follower_id: int, following_id: int) -> bool:
        resp = self._db.table("soul_links").select("link_id").eq("follower_id", follower_id).eq("following_id", following_id).execute()
        return bool(resp.data)
