
from typing import Dict, Optional, List
from src.config import get_supabase

class PostDAO:
    def __init__(self):
        self._db = get_supabase()

  
    
    
    
    
    
    
    
    def create(self, user_id: int, content: str, image_url: str = None, video_url: str = None):
        data = {
            "user_id": user_id,
            "content": content,
            "image_url": image_url,
            "video_url": video_url
        }
        resp = self._db.table("posts").insert(data).execute()
        return resp.data

    def list_recent(self, limit=50):
        resp = self._db.table("posts").select("*").order("created_at", desc=True).limit(limit).execute()
        return resp.data
    
    
    
    
    
    
    
    
    

    def get_by_id(self, post_id: int) -> Optional[Dict]:
        resp = self._db.table("posts").select("*").eq("post_id", post_id).limit(1).execute()
        return resp.data[0] if resp.data else None

    
    def update(self, post_id: int, updates: Dict) -> Optional[Dict]:
        self._db.table("posts").update(updates).eq("post_id", post_id).execute()
        return self.get_by_id(post_id)

    def delete(self, post_id: int) -> bool:
        self._db.table("posts").delete().eq("post_id", post_id).execute()
        return True

    def like(self, post_id: int) -> Optional[Dict]:
        # Increment likes
        self._db.rpc("increment_likes", {"p_post_id": post_id}).execute()  # or raw update if function not present
        return self.get_by_id(post_id)


