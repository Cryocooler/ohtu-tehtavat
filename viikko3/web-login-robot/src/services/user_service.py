from entities.user import User
import re
from repositories.user_repository import (
    user_repository as default_user_repository
)


class UserInputError(Exception):
    pass


class AuthenticationError(Exception):
    pass


class UserService:
    def __init__(self, user_repository=default_user_repository):
        self._user_repository = user_repository

    def check_credentials(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")

        user = self._user_repository.find_by_username(username)

        if not user or user.password != password:
            raise AuthenticationError("Invalid username or password")

        return user

    def create_user(self, username, password, password_confirmation):
        self.validate(username, password, password_confirmation)

        user = self._user_repository.create(
            User(username, password)
        )

        return user

    def validate(self, username, password, password_confirmation):
        if not username or not password:
            raise UserInputError("Username and password are required")

        # toteuta loput tarkastukset tänne ja nosta virhe virhetilanteissa
        if not (len(username) > 3):
            print('condition triggered')
            raise UserInputError('Username is too short')
        elif not re.match("[a-z]*", username):
            raise UserInputError('Username must contain only letters a-z')

        if not len(password) >= 8:
            raise UserInputError('Password is too short')
        elif not  re.match("^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$", password):
            raise UserInputError('Password must contain letters a-z and numbers')

        if password_confirmation !=  password:
            raise UserInputError('Password and confirmation do not match')



user_service = UserService()
