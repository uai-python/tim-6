from config import db

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

class Quiz(db.Model):
    __tablename__ = 'quiz'

    idquiz = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String(45))
    jumlah_soal = db.Column(db.String(45))
    WaktuMasuk = db.Column(db.String(45))
    WaktuAkhir = db.Column(db.String(45))
    score = db.Column(db.String(45))

    def __init__(self, user, jumlah_soal, WaktuMasuk, WaktuAkhir, score):
        self.user = user
        self.jumlah_soal = jumlah_soal
        self.WaktuMasuk = WaktuMasuk
        self.WaktuAkhir = WaktuAkhir
        self.score = score

    def __repr__(self):
        return '<Quiz %r>' % self.user