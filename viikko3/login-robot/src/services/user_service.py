from entities.user import User
import re


class UserInputError(Exception):
    pass


class AuthenticationError(Exception):
    pass


class UserService:
    def __init__(self, user_repository):
        self._user_repository = user_repository

    def check_credentials(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")

        user = self._user_repository.find_by_username(username)

        if not user or user.password != password:
            raise AuthenticationError("Invalid username or password")

        return user

    def create_user(self, username, password):
        self.validate(username, password)

        user = self._user_repository.create(
            User(username, password)
        )

        return user

    def validate(self, username, password):
        #print('password check', re.match("^[a-z, 0-9]*", password))
        if not username or not password:
            raise UserInputError("Username and password are required")

        # if not re.match("^[a-z]{3,}$",username):
        #     raise UserInputError('Username must contain at least 3 letters')
        # if not re.match("^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$", password):
        #     raise UserInputError('Password must containt at least 8 characters with numbers and letters')

        #username check 1:
        if not (len(username) > 3):
            print('condition triggered')
            raise UserInputError('Username is too short')
        elif not re.match("[a-z]*", username):
            raise UserInputError('Username must contain only letters a-z')

        if not len(password) >= 8:
            raise UserInputError('Password is too short')
        elif not  re.match("^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$", password):
            raise UserInputError('Password must contain letters a-z and numbers')
        #toteuta loput tarkastukset tänne ja nosta virhe virhetilanteissa
        # if  len(username) < 3 or len(password) < 8:  #not re.match("^[a-z]", password):
        #     #print(len(username))
        #     #print(re.match("^[a-z]+$", username))
        #     #print(re.match("^[a-z]", password))
        #     raise UserInputError("Username and password must contain enough characters")
        # if not re.match("[a-z, 0-9]*", password) or not re.match("^[a-z]*", username):
        #         raise UserInputError("Invalid password or username")


