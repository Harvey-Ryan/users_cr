#server.py
from flask_app import app 
from flask_app.controllers import users

# ...server.py

# @app.route("/")
# def index():
#     return render_template("index.html")

# @app.route("/submit",methods=["POST"])
# def submit():

#     request.form['action'] == 'submit'
#         # Collect data and send to DB
#     data={
#         'first_name': request.form['f_name'],
#         'last_name':request.form['l_name'],
#         'email':request.form['email'],
#     }

#     id = User.save(data)
#     print(f"THIS IS THE ID: {id}")
#     session['user_id'] = id
#     return redirect("/dash")#<<<<<<<<<<<<<<<<<
    # else:
    #     this_user = User.get_one_by_email(request.form['email']) ######################
    #     if not this_user:                                        #        Login       #
    #         return redirect('/')                                 #        Logic       #
    #     if this_user.password == request.form['password']:       ######################
    #         session['user_id'] = this_user.id
    #         return redirect('/dash')
    #return redirect("/")


# @app.route("/dash")
# def dash():
#     users = User.get_all()
#     return render_template("dash.html",users=users)


# @app.route('/users/<int:id>/edit')
# def edit_view(id):
#     return render_template("update.html",user=User.get_one_by_id(id))

# @app.route('/users/<int:id>/update',methods=['POST'])
# def  update_user(id):
#     data={
#         'first_name':request.form['first_name'],
#         'last_name':request.form['last_name'],
#         'email':request.form['email'],
#         'password':request.form['password']
#         }
#     User.update(data)
#     return redirect('/')

# @app.route("/users/<int:id>/destroy")
# def delete(id):
#     User.delete(id)
#     return redirect("/dash")


if __name__ == "__main__":
    app.run(debug=True)

