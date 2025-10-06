

from typing import Dict, List, Optional
from src.dao.post_dao import PostDAO
from src.services.reverberation_service import ReverberationService

class PostService:
    dao = PostDAO()

   
    @classmethod
    def create(cls, user_id: int, content: str, image_url: str = None, video_url: str = None):
        return cls.dao.create(user_id, content, image_url, video_url)

    @classmethod
    def get(cls, post_id: int) -> Optional[Dict]:
        return cls.dao.get_by_id(post_id)

 
    @classmethod
    def update(cls, post_id: int, updates: Dict) -> Optional[Dict]:
        return cls.dao.update(post_id, updates)

    @classmethod
    def delete(cls, post_id: int) -> bool:
        return cls.dao.delete(post_id)

    @classmethod
    def like(cls, post_id: int) -> Optional[Dict]:
        return cls.dao.like(post_id)
    @classmethod
    def list_recent(cls, limit=50):
        posts = cls.dao.list_recent(limit) or []
        for p in posts:
            p['comment_count'] = len(ReverberationService.list_post(p['post_id']))
            p['echo_count'] = p.get('echo_count', 0)
        return posts
    
    
    
   

    
