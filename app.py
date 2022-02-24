# from flask import Flask  
# app = Flask(__name__)  
# #@app.route("<local_host>/<route_destination>/<*next_routedestination>")  #defualts to localhost
# @app.route("/")  
# def hello():  
#     return "<p>Hello, World</p>";  
  
# if __name__ =="__main__":  
#     app.run(debug = True)  
import datetime
from flask import Flask, render_template, redirect
app=Flask(__name__,)

# @app.route('/')
# def index():
#     return 'Web App with python Flask!'

@app.route('/about')
def about():
    return render_template('about.html')
@app.route('/home')
def home():
    return render_template('home.html')

if __name__ =="__main__":  
    app.run(debug = True)  