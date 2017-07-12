from flask import Flask 
from flask_admin import Admin, BaseView, expose


app = Flask(__name__)
admin = Admin(app, name='God Area')

class Myview(BaseView):
	@expose('/')
	def admin(self):
		return self.render('admin.html')

admin.add_view(Myview(name='user'))


from flask import Blueprint
admin = Blueprint('admin', __name__)
