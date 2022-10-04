import bcrypt
from flask import Flask, render_template, request, session, redirect, url_for
from secret.secret import Secret
#-----------------------------------------------------
app = Flask(__name__)
app.secret_key = Secret.session_secret_key
db = pymysql.connect(host=Secret.db_host, port=Secret.db_port, user=Secret.db_user, passwd=Secret.db_passwd, db=Secret.db_name, charset='utf8')
cur = db.cursor()
#-----------------------------------------------------
app.secret_key = Secret.app_secret_key
app.config['UPLOAD_FOLDER'] = Secret.workspace
#-----------------------------------------------------
@app.route("/")
def root():
	session.clear()
	return redirect(url_for('home'))

if __name__ == "__main__":
	app.debug = True
	app.run(debug=True)