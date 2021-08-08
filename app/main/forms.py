from flask_wtf import Form
from wtforms.fields import StringField, SubmitField
from wtforms.validators import Required


class LoginForm(Form):
    """Accepts a nickname and a room."""
    name = StringField('имя', validators=[Required()])
    room = StringField('комната', validators=[Required()])
    submit = SubmitField('войти в комнату')
