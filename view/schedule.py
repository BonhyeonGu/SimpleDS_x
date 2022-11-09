from flask import Blueprint, session, redirect, url_for, render_template
schedule = Blueprint("schedule", __name__, url_prefix="/schedule")

#클라이언트 아이디 입력있는, 설정가능한 프론트
@schedule.route("/")
def index():
	if not 'no' in session:
		return redirect(url_for('login'))
	location = "files" + session['id']
	names, dates_edit = u.outDirList(location)
	return render_template('file_setting.html', names=names, dates_edit=dates_edit, use=u.outDirByte(location))

#해당 아이디에 속한 스케줄 json전송
@schedule.route("/jsonFileList")
def jsonFileList():
	if not 'no' in session:
		return redirect(url_for('login'))
	location = "files" + session['id']
	names, dates_edit = u.outDirList(location)
	return render_template('file_setting.html', names=names, dates_edit=dates_edit, use=u.outDirByte(location))

#해당 아이디에 속한 스케줄을 전송된 스케줄로 덮어씀, 디비와 소통
@schedule.route("/edit", methods=['POST'])
def upload():
	if not 'no' in session:
		return redirect(url_for('login'))
	location = "files" + session['id']
	file = request.files['file']
	
	file.save(u.pathJoin(location, file.filename))
	return redirect(url_for('file_setting'))
