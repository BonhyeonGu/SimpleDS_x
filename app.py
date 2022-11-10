from flask import redirect, url_for, render_template
from view import app

@app.route("/")
def root():
	return redirect(url_for('index'))

@app.route("/index")
def index():
	return render_template('index.html')

if __name__ == "__main__":
	app.run(debug=True)