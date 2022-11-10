from flask import Flask
from . import file
from . import schedule

app = Flask(__name__)
app.register_blueprint(file.file)
app.register_blueprint(schedule.schedule)

#app.config['UPLOAD_FOLDER'] = Secret.workspace
#-----------------------------------------------------