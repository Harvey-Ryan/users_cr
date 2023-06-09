
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re
from flask_app import app
# from flask_bcrypt import Bcrypt
db = "users_cr"

# bcrypt = Bcrypt(app)
# EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class User:
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_one(cls,data):
        query = 'SELECT * FROM users WHERE id=%(id)s;'
        result = connectToMySQL(db).query_db(query,data)
        print("result[0] = ",result[0])
        user = cls(result[0])
        return user

    @classmethod
    def get_all(cls):
        query = 'SELECT * FROM users;'
        results = connectToMySQL(db).query_db(query)
        users = []
        for user in results:
            users.append(cls(user))
        return users

    @classmethod
    def save(cls,data):
        query = """
                INSERT INTO users (first_name, last_name, email)
                VALUES (%(first_name)s,%(last_name)s,%(email)s);
                """
        results = connectToMySQL(db).query_db(query,data)
        return results

    @classmethod
    def delete(cls,id):
        query = 'DELETE FROM users WHERE id=%(id)s;'
        connectToMySQL(db).query_db(query,{'id' : id})


    @classmethod
    def update(cls,data):
        query = """
                UPDATE users 
                SET first_name=%(first_name)s, last_name=%(last_name)s, email=%(email)s 
                WHERE id=%(id)s;
                """
        connectToMySQL(db).query_db(query,data)

    @classmethod
    def get_one_by_id(cls,id):
        data={
            'id':id
        }
        query="""
        SELECT * FROM users WHERE id = %(id)s;
        """
        results = connectToMySQL(db).query_db(query,data)
        return cls(results[0])