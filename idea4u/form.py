from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length


class IdeaForm(FlaskForm):
    topic = StringField('topic', validators=[DataRequired(), Length(1, 10)])
    idea = TextAreaField('idea', validators=[DataRequired(), Length(1, 50)])
    writer = StringField('writer', validators=[DataRequired(), Length(1, 10)])
    submit = SubmitField()


