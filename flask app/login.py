from flask import Flask,request,render_template,redirect,url_for
app = Flask(__name__)

@app.route('/success/<name>')
def success(name):
	return "welcome %s" % name

@app.route('/login/', methods=['GET', 'POST'])
def login():
	error = None
	if request.method == 'POST':
		user = request.form['username']
		return redirect(url_for('success',name = user))
	return render_template('sample.html', error=error)

if __name__ == "__main__":
	app.run(debug = True)
