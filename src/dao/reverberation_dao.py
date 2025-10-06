from src.config import get_supabase

class ReverberationDAO:
    def __init__(self):
        self._db = get_supabase()

    # Create a comment for thought OR post
    def create(self, viber_id: int, content: str, thought_id: int = None, post_id: int = None):
        data = {
            "viber_id": viber_id,
            "content": content,
            "thought_id": thought_id,
            "post_id": post_id
        }
        resp = self._db.table("reverberations").insert(data).execute()
        return resp.data

    # List comments by thought
    def list_by_thought(self, thought_id: int):
        resp = self._db.table("reverberations").select("*").eq("thought_id", thought_id).execute()
        return resp.data

    # NEW: List comments by post
    def list_by_post(self, post_id: int):
        resp = self._db.table("reverberations").select("*").eq("post_id", post_id).execute()
        return resp.data

    # Optional: list all reverberations (for trending calculation)
    def list_all(self):
        resp = self._db.table("reverberations").select("*").execute()
        return resp.data


    def list_by_post(self, post_id: int):
        resp = self._db.table("post_comments").select("*").eq("post_id", post_id).order("created_at", desc=True).execute()
        return resp.data

    def create_post_comment(self, post_id: int, viber_id: int, content: str):
        resp = self._db.table("post_comments").insert({
            "post_id": post_id,
            "viber_id": viber_id,
            "content": content
        }).execute()
        return resp.data
