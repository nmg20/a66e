from app.models import db
from app.models.user import User

class UserDAO:
    @staticmethod
    def get_user_by_id(id):
        return User.query.get(id)

    @staticmethod
    def create_user(username, email):
        user = User(
            username = username,
            email = email
            )
        db.session.add(user)
        db.session.commit()
        return user