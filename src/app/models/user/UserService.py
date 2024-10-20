from app.models.user import UserDAO

class UserService:
    @staticmethod
    def register_user(username, email):
        # Lógica de validación
        return UserDAO.create_user(username, email)

    @staticmethod
    def get_user(id):
        return UserDAO.get_user_by_id(id)