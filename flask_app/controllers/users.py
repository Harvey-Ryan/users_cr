
from flask_app import app	
from flask import render_template,redirect,request,session,flash
from flask_app.models.user import User
# from flask_bcrypt import Bcrypt
# bcrypt = Bcrypt(app)

@app.route("/")
def index():
    return render_template("index.html")

# @app.route('/')
# def index():
#     users = User.get_all()
#     return render_template('index.html', users=users)

@app.route("/dash")
def dash():
    users = User.get_all()
    return render_template("dash.html",users=users)

@app.route("/submit",methods=["POST"])
def submit():

    request.form['action'] == 'submit'
        # Collect data and send to DB
    data={
        'first_name': request.form['first_name'],
        'last_name':request.form['last_name'],
        'email':request.form['email'],
    }
    id = User.save(data)
    print(f"THIS IS THE ID: {id}")
    session['user_id'] = id
    return redirect("/profile/" + str(id))

@app.route("/profile/<int:id>")
def profile(id):
    data={
        'id':id
    }
    users = User.get_one(data)
    return render_template("profile.html", user=users)

@app.route('/users/<int:id>/edit')
def edit_view(id):
    return render_template("update.html",user=User.get_one_by_id(id))

@app.route('/users/<int:id>/update',methods=['POST'])
def  update_user(id):
    data={
        'id':id,
        'first_name':request.form['first_name'],
        'last_name':request.form['last_name'],
        'email':request.form['email']
        }
    User.update(data)
    return render_template("profile.html",user=User.get_one_by_id(id))

@app.route("/users/<int:id>/destroy")
def delete(id):
    User.delete(id)
    return redirect("/dash")






# from flask_app import app	
# from flask import render_template,redirect,request,session,flash
# from flask_app.controllers.users import User
# # from mysqlconnection import connectToMySQL


# class User: # CREATE

#     db="users_cr"

#     def __init__(self,data):
#         self.id = data['id']
#         self.first_name = data['first_name']
#         self.last_name=data['last_name']
#         self.email=data['email']
#         self.created_at=data['created_at']
#         self.updated_at=data['updated_at']
    # @classmethod
    # def get_one_by_id(cls,id):
    #     data={
    #         'id':id
    #     }
    #     query="""
    #     SELECT * FROM users WHERE id = %(id)s;
    #     """
    #     results = connectToMySQL(cls.db).query_db(query,data)
    #     return cls(results[0])

#     @classmethod # READ
#     def get_all(cls):
#         query="SELECT * FROM users;"
#         results = connectToMySQL(cls.db).query_db(query)
#         print(results)
#         users =[]
#         for row in results:
#             users.append(cls(row)) #feeds into the constructor on line 8.
#         return users

#     @classmethod
#     def save(cls,data):
#         query = """
#         INSERT INTO users(first_name,last_name,email) 
#         VALUES(%(first_name)s,%(last_name)s,%(email)s);
#         """ # """ allows you to break up the line of code into multiple lines.
#         results = connectToMySQL(cls.db).query_db(query,data)
#         return results
    
#     @classmethod                        # PASSES INFORMATION TO SUBMIT ROUTE
#     def get_one_by_email(cls,email):    # ON server.py FOR LOGIN CREDENTIALS
#                                         # TO ISOLATE SINGLE OUT 1 DICTIONARY
#         data={
#             'email':email
#         }
#         query="""
#         SELECT * FROM users WHERE email = %(email)s;
#         """
#         results = connectToMySQL(cls.db).query_db(query,data)
#         return cls(results[0])
    
    
#     @classmethod
#     def update(cls, data):
#         query = """
#         UPDATE users SET 
#         first_name = %(first_name)s, 
#         last_name = %(last_name)s, 
#         email = %(email)s 
#         WHERE id = %(id)s;
#         """
#         results = connectToMySQL(cls.db).query_db(query, data)
#         return results
    
#     @classmethod
#     def delete(cls,id):
#         data={
#             'id':id
#         }
#         query="""
#         DELETE FROM users
#         WHERE id=%(id)s;
#         """
#         results = connectToMySQL(cls.db).query_db(query, data)
#         return results