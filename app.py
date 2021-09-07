from flask import Flask, request, render_template, redirect, url_for, Markup 
from flask_restful import Resource, Api, abort, reqparse
from datetime import date
import sqlite3

app = Flask(__name__)
# db = SQLAlchemy(app)
# app.config["SQLAlCHEMY_DATABASE_URI"] = "sqlite///database.db"

# class moodModel(db.Model):
#     date = db.Column(db.String, primary_key=True)
#     mood = db.Column(db.String, nullable=True)

#     def __repr__(self):
#         return f"{today} = {feeling}"

# def create_database():
#     return db.create_all()
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
        if user == valid_username and passkey == valid_password:
            return redirect(url_for("mood", profile = user))
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

@app.route('/mood', methods=["POST", "GET"])
def mood():
    if request.method == "POST":
        current_mood = request.form["feeling"]
        today = date.today()
        current_date = today.strftime("%B %d, %Y")

        with sqlite3.connect("mood.db") as con:
            cur = con.cursor()
            cur.execute("select * from Timeline")  
            rows = cur.fetchall()
            try:
                if len(rows) == 0:
                    streak_counter = 0
                    if current_mood == "":
                        streak_counter = 0
                    else:
                        pass
                else:
                    streak_counter = rows[-1][2]
                    if current_mood == "":
                        streak_counter = 1
                    else:
                        streak_counter += 1
            except:
                pass                       

            cur.execute("INSERT or IGNORE into Timeline(today_date, mood, streak_counter) values (?,?,?)", (current_date, current_mood, streak_counter))
            con.commit()
        # con.row_factory = sqlite3.Row          
        cur.execute("select * from Timeline")  
        rows = cur.fetchall()

        response = '''Thank you for your response!'''

        if streak_counter > 1:
            streak = f'''You're on a streak of {streak_counter}!'''
            return render_template("Mood.html", rows=rows, question=response, streak=streak)
        else:
            return render_template("Mood.html", rows=rows, question=response)    
        con.close() 

    else:
        question = '''How are you feeling today?'''
        input_line = Markup('''<input type="text" name="feeling" size="50" />''')        
        with sqlite3.connect("mood.db") as con:
            cur = con.cursor()
        # con.row_factory = sqlite3.Row          
        cur.execute("select * from Timeline")  
        rows = cur.fetchall()
        return render_template("Mood.html", rows=rows, question=question, input=input_line)
        con.close() 

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



