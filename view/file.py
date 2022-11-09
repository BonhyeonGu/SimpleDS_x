from flask import Blueprint, session, redirect, url_for, render_template
file = Blueprint("file", __name__, url_prefix="/file")

#클라이언트 아이디 입력
@file.route("/")
def index():
	if not 'no' in session:
		return redirect(url_for('login'))
	location = "files" + session['id']
	names, dates_edit = u.outDirList(location)
	return render_template('file_setting.html', names=names, dates_edit=dates_edit, use=u.outDirByte(location))

#해당 아이디에 속한 파일리스트 json출력
@file.route("/jsonFileList")
def jsonFileList():
	if not 'no' in session:
		return redirect(url_for('login'))
	location = "files" + session['id']
	names, dates_edit = u.outDirList(location)
	return render_template('file_setting.html', names=names, dates_edit=dates_edit, use=u.outDirByte(location))

#해당 아이디에 속한 파일리스트에 파일업로드
@file.route("/upload", methods=['POST'])
def upload():
	if not 'no' in session:
		return redirect(url_for('login'))
	location = "files" + session['id']
	file = request.files['file']
	
	file.save(u.pathJoin(location, file.filename))
	return redirect(url_for('file_setting'))
