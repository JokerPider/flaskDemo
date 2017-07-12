from flask import Flask, request, render_template, redirect, url_for
from form import writeBlog

app = Flask(__name__)
app.config.from_object('config')

datas = [  #fake datas, use sqlite3 later
	{
	'title':'title1', 
	'centent':'content1'
	},
	{
	'title':'title2', 
	'centent':'content2'
	},
	{
	'title':'title3', 
	'centent':'content3'
	}
]

@app.route('/')
@app.route('/index/')
def index():
	return render_template('index.html', datas = datas)


@app.route('/writeBlog', methods=['Get', 'POST'])
def write():
	form = writeBlog()
	title = ''
	content = ''
	if form.validate_on_submit():
		title = form.title.data
		content = form.content.data
		datas.append({'title':title, 'centent':centent})
		form.title.data, form.content.data = '', ''
		return redirect(url_for('index.html'))
	return render_template('form.html', form=form)

#add expose
from admin import admin
app.register_blueprint(admin, url_prefix='/admin')

if __name__ == '__main__':
	app.run(debug=True)