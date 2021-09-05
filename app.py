from flask import Flask, request, render_template, redirect, url_for, Markup 
from flask_restful import Resource, Api, abort, reqparse
import datetime


app = Flask(__name__)
# api = Api(app)

# login_put = reqparse.RequestParser()
# login_put.add_argument("username", type=str, help="Request Username", required=True)
# login_put.add_argument("password", type=str, help="Request Password", required=True)

# names = {}


# class Login(Resource):
#     def get(self, credentials):
#         return {"data":"name"}

#     def post(self, credentials):
#          return {"data":"posted"}

#     def put(self, credentials):
#         print(request.form["username"])
#         args = login_put.parse_args()
#         return {credentials:args}       

# api.add_resource(Login, "/login/<string:credentials>")

valid_username = "john_doe123"
valid_password = "P45Sw0rd"

# @app.route("/")
# def home():
#     return render_template("Home.html")   

@app.route('/', methods=["POST", "GET"])
def login():
    if request.method == "POST":
        user = request.form["username"]
        passkey = request.form["password"]
        if user == valid_username and key == valid_password:
            return redirect(url_for("mood", profile = f"Welcome {user}"))
        else:
            if user == "" or passkey == "":
                error_msg_user = ""
                error_msg_pass = ""
                user_error = None
                passkey_error = None     
                if user == "":
                    user_error = True
                    error_msg_user = "*Please enter your username"
                if passkey == "":
                    passkey_error = True
                    error_msg_pass = "*Please enter your password"
                if user_error == True == passkey_error:
                    error_msg = Markup(f"{error_msg_user}<br/>{error_msg_pass}<b/>")
                else:
                    error_msg = error_msg_pass + error_msg_user
                    error_msg = Markup(f"{error_msg}</b>")         
                return render_template("Login.html", error_msg=error_msg)
            else:            
                if " " != user != valid_username and " " != passkey != valid_username:   
                    return render_template("Login.html", error_msg="*Incorrect username or password")
    else:
        return render_template("Login.html", error_msg="")    

# @app.route('/create')
# def create():
#     return render_template("create.html")

@app.route('/mood/<profile>')
def mood(profile):
    return f"<h1>{profile}</h1>"    


# @app.route("/<mood>")
# def user(mood):
#     return f"hello {mood}!"

# @app.route("/admin")
# def admin():
#     return redirect(url_for("index"))

# @app.route("/login", method=["GET", "POST"])
# def login():
#     return "Hello world"

# @app.route("/create", method=["GET", "POST"])
# def create():
#     return render_template()    

# @app.route("/<usr>")
# def user(usr):
#     return f"<h1>{usr}<h1>"    

if __name__ == "__main__":
    app.run(debug=True)



