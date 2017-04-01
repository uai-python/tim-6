from flask import Flask, render_template, session, redirect, url_for, request, escape
from flask_sqlalchemy import SQLAlchemy
import mysql.connector
from mysql.connector import errorcode

app = Flask(__name__)
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:0110@localhost/webq'
#db = SQLAlchemy(app)

@app.route('/', methods=['GET','POST'])
def index():
    if 'user' in session:
        db = mysql.connector.connect(host='localhost', port='3306', database='webq', user='root', password='0110')
        cursor = db.cursor()
        cursor.execute("SELECT question FROM question ORDER BY RAND() LIMIT 1")
        data = cursor.fetchall()

        username_session = escape(session['user']).capitalize()
        number = 0
        return render_template('web.html', user=username_session, data = data, number = number + 1)
    else:
        return redirect(url_for("login"))

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        session['user'] = request.form['user']
        user = request.form['user']
        usia = request.form['usia']
        jenis_kelamin = request.form['jenis_kelamin']
        kota = request.form['kota']

        db = mysql.connector.connect(host='localhost', port='3306', database='webq', user='root', password='0110')
        cursor = db.cursor()
        cursor.execute("INSERT INTO guest(usia, jenis_kelamin, kota, user) VALUES (%s, %s, %s, %s)", (usia, jenis_kelamin, kota, user))
        db.commit()
        return redirect(url_for("index"))
    else:
        return render_template('index.html', title='home')

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('user', None)
    return redirect(url_for('index'))

@app.route('/result', methods=['POST', 'GET'])
def result():
    return render_template('result.html', title='Quiz')

@app.errorhandler(404)
def not_found(error):
    return 'Page not found!', 404

# set the secret key.  keep this really secret:
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

if __name__ == "__main__":
    app.run(host='0.0.0.0')