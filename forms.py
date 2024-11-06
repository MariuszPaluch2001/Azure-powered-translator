from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField, SelectField
from wtforms.validators import DataRequired


class TranslateForm(FlaskForm):
    lang_from = SelectField("Language from", choices=[])

    lang_to = SelectField("Language to", choices=[])

    text = TextAreaField("Text", validators=[DataRequired()])

    submit = SubmitField("Translate")
