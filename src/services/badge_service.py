

from src.dao.badge_dao import BadgeDAO

class BadgeService:
    dao = BadgeDAO()

    @classmethod
    def create(cls, name: str, description: str, aura_color: str, vibe_level: int):
        return cls.dao.create(name, description, aura_color, vibe_level)

    @classmethod
    def list(cls):
        return cls.dao.list()
    
    
    @classmethod
    def award(cls, user_id: int, badge_name: str):
        # Add badge to user's badges table
        return cls.dao.award_to_user(user_id, badge_name)
