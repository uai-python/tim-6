import db

class Guest(db.Model):
    idguess = db.Column(db.Integer, primary_key=True)
    usia = db.Column(db.Integer(11))
    jenis_kelamin = db.Column(db.Varchar(15))
    kota = db.Column(db.Varchar(45))
    user = db.Column(db.Varchar(45))

    def __init__(self, idguess, usia, jenis_kelamin, kota, user):
        self.idguess = idguess
        self.usia = usia
        self.jenis_kelamin = jenis_kelamin
        self.kota = kota
        self.user = user