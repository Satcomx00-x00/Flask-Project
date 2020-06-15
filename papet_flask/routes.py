from papet_flask import app, db
from flask import Flask, render_template, flash, redirect, url_for, session, logging, request
from papet_flask.models import Clients


# @app.route("/select")
# def select():
# 	return render_template('select.html', Clients = client.query.all() )

# @app.route('/new', methods = ['GET', 'POST'])
# def new():
#    if request.method == 'POST':
#       if not request.form['firstname'] or not request.form['lastname'] or not request.form['address1'] or not request.form['city']  or not request.form['username'] or not request.form['password']:
#          flash('Please enter all the fields', 'error')
#       else:
#          customers = Customers(request.form['firstname'], request.form['lastname'],
#             request.form['address1'], request.form['city'], request.form['state'], request.form['zip']
# 			, request.form['country'], request.form['username'], request.form['password'])
#
#          db.session.add(customers)
#          db.session.commit()
#          flash('Record was successfully added')
#    return render_template('new.html')


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        mail_client = request.form["mail_client"]
        password_client = request.form["password_client"]

        login = Clients.query.filter_by(mail_client=mail_client, password=password_client).first()
        if login is not None:
            return redirect(url_for("pld"))
    return render_template("login.html")


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == "POST":
        NOM_CLIENT = request.form['NOM_CLIENT']
        PRENOM_CLIENT = request.form['PRENOM_CLIENT']
        MAIL_CLIENT = request.form['MAIL_CLIENT']
        PASSWORD_CLIENT = request.form['PASSWORD_CLIENT']
        DEPARTEMENT_CLIENT = request.form['DEPARTEMENT_CLIENT']
        CODE_POSTAL = request.form['CODE_POSTAL']
        VILLE = request.form['VILLE']
        NUM_TEL = request.form['NUM_TEL']
        ID_PLD = request.form['ID_PLD']

        register = Clients(nom_client = NOM_CLIENT, prenom_client=PRENOM_CLIENT, mail_client = MAIL_CLIENT, password = PASSWORD_CLIENT, departement_client = DEPARTEMENT_CLIENT, code_postal = CODE_POSTAL, ville = VILLE, num_tel = NUM_TEL, id_pld = ID_PLD)
        db.session.add(register)
        db.session.commit()

        return redirect(url_for("login"))
    return render_template("register.html")

@app.route('/creationcolis', methods=['GET', 'POST'])
def creationcolis():
    if request.method == "POST":
        ID_COLIS = request.form['ID_COLIS']
        ID_CLIENT = request.form['ID_CLIENT']
        ID_ENTREPRISE = request.form['ID_ENTREPRISE']
        POID_COLIS = request.form['POID_COLIS']


        register = Colis(id_colis=ID_COLIS, id_client=ID_CLIENT, id_entreprise=ID_ENTREPRISE, poid_colis=POID_COLIS)
        db.session.add(register)
        db.session.commit()

        return redirect(url_for("creationcolis"))
    return render_template("pld.html")
@app.route("/")
def home():
    return render_template("acceuil.html", methods=['GET', 'POST'])

@app.route("/acceuil")
def acceuil():
    return render_template("acceuil.html", methods=['GET', 'POST'])



@app.route("/pld")
def pld():
    return render_template("pld.html", methods=['GET', 'POST'])

@app.route("/plrss")
def plrss():
    return render_template("plrss.html", methods=['GET', 'POST'])
