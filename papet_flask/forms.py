from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField, IntegerField
from wtforms.validators import DataRequired, InputRequired, Regexp,NumberRange

class CustomersForm(FlaskForm):
    nomclient = StringField('Nom',validators=[InputRequired(message='Veuillez saisir un nom !')])
    prenomclient = StringField('Prénom',[DataRequired()])
    paysclient = StringField('Pays',[DataRequired()])
    localiteclient = StringField('Localité',[DataRequired()])
    submit = SubmitField('Valider')
