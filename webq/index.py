from flask import Flask, render_template, session, redirect, url_for, request, escape
from flask_sqlalchemy import SQLAlchemy
import mysql.connector
from sqlalchemy import func

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:0110@localhost/webq'
app.debug=True
db = SQLAlchemy(app)

class Guest(db.Model):
    __tablename__ = 'guest'

    idguess = db.Column(db.Integer, primary_key=True)
    usia = db.Column(db.Integer)
    jenis_kelamin = db.Column(db.String(15))
    kota = db.Column(db.String(45))
    user = db.Column(db.String(45))

    def __init__(self, usia, jenis_kelamin, kota, user):
        self.usia = usia
        self.jenis_kelamin = jenis_kelamin
        self.kota = kota
        self.user = user

    def __repr__(self):
        return '<Guest %r>' % self.user

class Question(db.Model):
    __tablename__ = 'question'

    idquestion = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String)
    answer = db.Column(db.String(30))

    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

    def __repr__(self):
        return '<Question %r>' % self.question

@app.route('/', methods=['GET','POST'])
def index():
    if 'user' in session:
        fetch_data = Question.query.order_by(func.rand()).limit(1).all()
        return render_template('web.html', data=fetch_data)
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

        guest = Guest(usia, jenis_kelamin, kota, user)
        db.session.add(guest)
        db.session.commit()

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
    return render_template('dashboard.html', title='Dashboard')

@app.errorhandler(404)
def not_found(error):
    return 'Page not found!', 404

# set the secret key.  keep this really secret:
app.secret_key = 'Apa_hayo'

if __name__ == "__main__":
    app.run(host='0.0.0.0')