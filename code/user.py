import sqlite3

from flask_restful import Resource, reqparse


class User:
    def __init__(self, _id, username, password):
        self.id = _id
        self.username = username
        self.password = password

    @classmethod
    def find_by_username(cls, username):
        conn = sqlite3.connect("data.db")
        cursor = conn.cursor()

        query = "SELECT * FROM users WHERE username =?"
        result = cursor.execute(query, (username,))
        row = result.fetchone()
        if row:
            user = cls(*row)
        else:
            user = None
        conn.close()
        return user

    @classmethod
    def find_by_id(cls, _id):
        conn = sqlite3.connect("data.db")
        cursor = conn.cursor()

        query = "SELECT * FROM users WHERE id =?"
        result = cursor.execute(query, (_id,))
        row = result.fetchone()
        if row:
            user = cls(*row)
        else:
            user = None
        conn.close()
        return user


class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username', type=str, required=True, help="Enter unique username")
    parser.add_argument('password', type=str, required=True, help="Enter password")

    def post(self):
        data = UserRegister.parser.parse_args()
        if User.find_by_username(data['username']):
            return{"message":"A user with the given username already exists"}, 400
        conn = sqlite3.connect("data.db")
        cursor = conn.cursor()

        query = "Insert into users  values(NULL,?,?)"
        cursor.execute(query, (data["username"], data["password"]))

        conn.commit()
        conn.close()
        return {"message": "Successfully created users"}, 201
