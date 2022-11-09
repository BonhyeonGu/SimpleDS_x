#import bcrypt

#from secret.secret import Secret
#-----------------------------------------------------
#db = pymysql.connect(host=Secret.db_host, port=Secret.db_port, user=Secret.db_user, passwd=Secret.db_passwd, db=Secret.db_name, charset='utf8')
#cur = db.cursor()
#-----------------------------------------------------
from view import app
if __name__ == "__main__":
	app.run(debug=True)