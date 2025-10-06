

from src.config import get_supabase

class BadgeDAO:
    def __init__(self):
        self._db = get_supabase()

    def create(self, name: str, description: str, aura_color: str, vibe_level: int):
        resp = self._db.table("badges").insert({
            "name": name,
            "description": description,
            "aura_color": aura_color,
            "vibe_level_required": vibe_level
        }).execute()
        return resp.data

    def list(self):
        return self._db.table("badges").select("*").execute().data
    
    
    def award_to_user(self, user_id: int, badge_name: str):
        resp = self._db.table("user_badges").insert({
            "user_id": user_id,
            "badge_name": badge_name,
            "awarded_at": "now()"
        }).execute()
        return resp.data