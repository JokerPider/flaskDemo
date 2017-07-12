from flask.ext.wtf import Form
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import Required

class writeBlog(Form):
	title = StringField('write you title', validators = [Required()])
	content = TextAreaField('have a happy day~', validators = [Required()])
	submit = SubmitField('Submit')