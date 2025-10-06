from src.config import get_supabase

class EchoDAO:
    def __init__(self):
        self._db = get_supabase()

    def react(self, thought_id: int, viber_id: int, emotion: str):
        return self._db.table("echoes").insert({
            "thought_id": thought_id,
            "viber_id": viber_id,
            "emotion_tag": emotion
        }).execute().data

    def react_to_post(self, post_id: int, viber_id: int, emotion: str):
        return self._db.table("post_echoes").insert({
            "post_id": post_id,
            "viber_id": viber_id,
            "emotion": emotion
        }).execute().data
