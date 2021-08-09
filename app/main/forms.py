from flask_wtf import Form
from wtforms.fields import StringField, IntegerField, SubmitField
from wtforms.validators import Required, Length, NumberRange


class LoginForm(Form):
    """Accepts a nickname and a room."""
    name = StringField('Ваше имя:', validators=[Required(), Length(max=16, message="Слишком большое имя!")])
    room = IntegerField('Номер комнаты', validators=[NumberRange(min=0)])
    submit = SubmitField('войти в комнату')
