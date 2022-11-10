from flask import Blueprint, session, redirect, url_for, render_template
from pymongo import MongoClient
#------------------------------------------------------------------------
file = Blueprint("file", __name__, url_prefix="/file")
#------------------------------------------------------------------------

#------------------------------------------------------------------------
#!!! 입 또는 출력이 리스트인 경우는 사이즈가 1인 리스트의 경우를 포함함
@file.route("/")
def fileIndex():
	return render_template('fileIndex.html')

#현재 서버에 업로드된 파일들을 출력
#입력없음 출력리스트
@file.route("/jFilesOut2S")
def jFilesOut2S():
	location = "files" + session['id']
	names, dates_edit = u.outDirList(location)
	return render_template('file_setting.html', names=names, dates_edit=dates_edit, use=u.outDirByte(location))

#서버에 파일 업로드
#입력없음 출력없음
@file.route("/upload", methods=['POST'])
def upload():
	if not 'no' in session:
		return redirect(url_for('login'))
	location = "files" + session['id']
	file = request.files['file']
	
	file.save(u.pathJoin(location, file.filename))
	return redirect(url_for('file_setting'))

#서버에 업로드된 파일을 삭제 (GID가 사용중인지 확인? 또는 강제로?)
#입력리스트 출력없음
@file.route("/jsonG2Files")
def jsonG2Files():
	if not 'no' in session:
		return redirect(url_for('login'))
	location = "files" + session['id']
	names, dates_edit = u.outDirList(location)
	return render_template('file_setting.html', names=names, dates_edit=dates_edit, use=u.outDirByte(location))

#해당 GID가 '사용하고 있는' 파일들을 출력
#입력없음 출력리스트
@file.route("/jsonG2Files")
def jsonG2Files():
	if not 'no' in session:
		return redirect(url_for('login'))
	location = "files" + session['id']
	names, dates_edit = u.outDirList(location)
	return render_template('file_setting.html', names=names, dates_edit=dates_edit, use=u.outDirByte(location))

#해당 GID가 '사용하지 않는' 파일 a를 '사용하고 있는'으로 수정
#입력리스트 출력없음
@file.route("/jsonG2Files")
def jsonG2Files():
	if not 'no' in session:
		return redirect(url_for('login'))
	location = "files" + session['id']
	names, dates_edit = u.outDirList(location)
	return render_template('file_setting.html', names=names, dates_edit=dates_edit, use=u.outDirByte(location))

#해당 GID가 '사용하고 있는' 파일 a를 '사용하지 않는'으로 수정
#입력리스트 출력없음
@file.route("/jsonG2Files")
def jsonG2Files():
	if not 'no' in session:
		return redirect(url_for('login'))
	location = "files" + session['id']
	names, dates_edit = u.outDirList(location)
	return render_template('file_setting.html', names=names, dates_edit=dates_edit, use=u.outDirByte(location))