
from src.config import get_supabase

class TribeDAO:
    def __init__(self):
        self._db = get_supabase()

    def create(self, name, description):
        return self._db.table("tribes").insert({
            "name": name,
            "description": description
        }).execute().data

    def list(self):
        return self._db.table("tribes").select("*").execute().data

    def join(self, viber_id, tribe_id):
        # Check if already joined
        existing = self._db.table("viber_tribes")\
            .select("*")\
            .eq("viber_id", viber_id)\
            .eq("tribe_id", tribe_id)\
            .execute().data
        if existing:
            return {"message": "Already a member"}  # or raise custom exception
        return self._db.table("viber_tribes").insert({
            "viber_id": viber_id,
            "tribe_id": tribe_id
        }).execute().data


    def list_viber_tribes(self, viber_id):
        return self._db.table("viber_tribes").select("*").eq("viber_id", viber_id).execute().data

    # Updated list_members to include usernames
    def list_members(self, tribe_id):
        return self._db.table("viber_tribes")\
            .select("viber_id, vibers(username)")\
            .eq("tribe_id", tribe_id)\
            .execute().data

    def add_resource(self, tribe_id, viber_id, title, description, url):
        return self._db.table("tribe_resources").insert({
            "tribe_id": tribe_id,
            "viber_id": viber_id,
            "title": title,
            "description": description,
            "url": url
        }).execute().data

    def list_resources(self, tribe_id):
        return self._db.table("tribe_resources").select("*").eq("tribe_id", tribe_id).execute().data

    def follow_member(self, follower_id, followee_id, tribe_id):
        return self._db.table("tribe_follows").insert({
            "follower_id": follower_id,
            "followee_id": followee_id,
            "tribe_id": tribe_id
        }).execute().data

    def list_followed(self, follower_id, tribe_id):
        return self._db.table("tribe_follows").select("followee_id").eq("follower_id", follower_id).eq("tribe_id", tribe_id).execute().data
