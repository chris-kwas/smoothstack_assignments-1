from flask import Flask, redirect, render_template, url_for
from flask import request, make_response ,session

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['DEBUG'] = True
    
@app.route('/cookie', methods=['GET','POST'])  
def visit():
    #cookies is a dictiony
    #.get asks for specificed key(visit-count) if key doesnt exists creates it and sets value to second value (0)
    visit_count=request.cookies.get('visit-count', 0)#return string
    message =  "This is visit number {} ".format({int(visit_count)})
    resp = make_response(render_template('home.html', amt=message))#return http respose object
    vscount = int(visit_count) + 1
    resp.set_cookie('visit-count', str(vscount))#cookie values are strings
    return resp


@app.route('/login', methods=['GET','POST'])  
def login():
        if request.method == 'POST':
            person = request.form['name']#needs to be same variable name as in the html 
            session['name'] = person 
            return redirect(url_for('name', name=person))
        else:
            return render_template('login.html') 


@app.route("/name")
def name():
    if 'name' in session:
        name = session['name']
        return f'<h1>{name}</h1>'
    else:
        return  redirect(url_for('login'))




if __name__ == '__main__':
    app.run()