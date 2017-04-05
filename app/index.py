from flask import Flask, render_template, session, redirect, url_for, request
from sqlalchemy import func
from models import Question, Guest
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.debug=True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:0110@localhost/webq'

db = SQLAlchemy(app)

@app.route('/', methods=['GET','POST'])
def index():
    if 'user' in session:
        user = session['user']
        return render_template('index.html', user=user)
    else:
        return redirect(url_for("login"))

@app.route('/link', methods=['GET', 'POST'])
def link():
    fetch_data = Question.query.order_by(func.rand()).limit(1).all()
    user = session['user']
    Total_Soal = 0
    Total_jawab_benar = 0
    if request.method == 'POST':
        Total_Soal = request.form['total']
        Total_jawab_benar = 0

        fetch_data = Question.query.order_by(func.rand()).limit(1).all()
        user = session['user']
        return render_template('web.html', data=fetch_data, user=user, Total_Soal=Total_Soal, Total_jawab_benar=Total_jawab_benar)
    return render_template('web.html', data=fetch_data, user=user, Total_Soal=Total_Soal, Total_jawab_benar=Total_jawab_benar)

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
        return render_template('login.html', title='home')

@app.route('/cek', methods=['GET','POST'])
def cek():
    total = 0
    hasil = 0


    if request.method == 'POST':
        jawab_asli = request.form['jawaban']
        ask = request.form['pertanyaan']
        jawab_user = request.form['answer']
        user = session['user']

        jumlah = int(request.form['soal_ke']) + 1

        if jumlah > 10:
            return render_template('result.html', title='Cek', jawab_asli=jawab_asli, jawab_user=jawab_user, ask=ask,
                                   user=user, total=total, hasil=hasil, jumlah=jumlah)

        if jawab_asli == jawab_user:
            hasil = hasil + 1
        elif jawab_asli != jawab_user:
            hasil = hasil + 0

    return render_template('cek.html', title='Cek', jawab_asli=jawab_asli, jawab_user=jawab_user, ask=ask, user=user, total=total, hasil=hasil, jumlah=jumlah)

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('user', None)
    return redirect(url_for('index'))

@app.errorhandler(404)
def not_found(error):
    return 'Page not found!', 404

# set the secret key.  keep this really secret:
app.secret_key = 'Apa_hayo'

if __name__ == "__main__":
    app.run(host='0.0.0.0')