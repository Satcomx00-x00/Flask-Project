from papet_flask import db

class Clients(db.Model):

    __tablename__ = 'client'

    id_client = db.Column(db.Integer,nullable=False, autoincrement=True, primary_key=True)
    id_pld = db.Column(db.String(3), nullable=False)
    nom_client = db.Column(db.String(50), nullable=False)
    prenom_client = db.Column(db.String(50), nullable=False)
    departement_client = db.Column(db.String(50), nullable=False)
    mail_client = db.Column(db.String(50), nullable=False)
    code_postal = db.Column(db.Integer, nullable=False)
    ville = db.Column(db.String(50), nullable=False)
    num_tel = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(50), nullable=False)

class Colis(db.Model):

    __tablename__ = 'colis'

    id_colis = db.Column(db.Integer, nullable=False, autoincrement=True, primary_key=True)
    id_client = db.Column(db.Integer, nullable=False)
    id_entreprise = db.Column(db.Integer, nullable=False)
    poid_colis = db.Column(db.Float, nullable=False)

class Entreprise(db.Model):

    __tablename__ = 'entreprise'

    id_entreprise = db.Column(db.Integer,nullable=False, autoincrement=True, primary_key=True)
    id_pld = db.Column(db.String(3), nullable=False)
    nom_entreprise = db.Column(db.String(100), nullable=False)
    departement_entreprise = db.Column(db.String(100), nullable=False)
    ville_entreprise = db.Column(db.String(100), nullable=False)
