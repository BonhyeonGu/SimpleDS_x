from flask import Blueprint, session, redirect, url_for, render_template, jsonify, request
from werkzeug.utils import secure_filename
from pymongo import MongoClient
from os import listdir, remove
from datetime import datetime
import cv2
#------------------------------------------------------------------------
from secret.secret import mongo_dbid, mongo_dbpw, mongo_dbaddr, mongo_dbport
#------------------------------------------------------------------------
file = Blueprint("file", __name__, url_prefix="/file")
#------------------------------------------------------------------------
client = MongoClient(host=mongo_dbaddr, port=mongo_dbport, username=mongo_dbid, password=mongo_dbpw)
db = client['ds']
col_uf = db['uploaded_file']
col_f4g = db['file4group']
col_s4g = db['schedule4group']
LOCATION = './files/'

#------------------------------------------------------------------------
def get_duration(filename):
    video = cv2.VideoCapture(filename)
    return video.get(cv2.CAP_PROP_POS_MSEC)
#------------------------------------------------------------------------
#!!! 입 또는 출력이 리스트인 경우는 사이즈가 1인 리스트의 경우를 포함함
#앞글자가 a인 것은 출력이 중요하지 않음, j는 출력이 중요함

@file.route("/")
def fileIndex():
	return render_template('fileIndex.html')

#현재 서버에 업로드된 파일들을 출력
#입력없음 출력리스트
@file.route("/jFilesOut2S", methods=['POST'])
def jFilesOut2S():
	ret = listdir(LOCATION)
	j = {"ret" : ret}
	return jsonify(j)

#서버에 파일 업로드, 얘는 json아니고 리플래시를 요구함
#입력파일 출력없음
@file.route("/upload", methods=['POST'])
def upload():
	inp_file = request.files['file']
	inp_des = request.files['des']
	nowDate = datetime.today().strftime("%Y%m%d%H%M%S")
	inp_file.
	inp_file.save(LOCATION + secure_filename(inp_file.filename))
	doc = {
		"name" : inp_file,
		"des" : 
	}
	col_uf.insert_one(doc)
	return render_template('fileIndex.html')

#서버에 업로드된 파일을 삭제 (GID가 사용중인지 확인? 또는 강제로?)
#입력{gid, 파일리스트} 출력없음
@file.route("/aDeleteFiles", methods=['POST'])
def aDeleteFiles():
	params = request.get_json()
	fileName = params['fileName']
	print(fileName)
	remove(LOCATION + fileName)
	return jsonify({"msg" : 'clear'})

#해당 GID가 '사용하고 있는' 파일들을 출력
#입력gid 출력리스트
@file.route("/jUsedFiles")
def jUsedFiles():
	if not 'no' in session:
		return redirect(url_for('login'))
	location = "files" + session['id']
	names, dates_edit = u.outDirList(location)
	return render_template('file_setting.html', names=names, dates_edit=dates_edit, use=u.outDirByte(location))

#해당 GID가 '사용하지 않는' 파일 a를 '사용하고 있는'으로 수정
#입력{gid, 파일리스트} 출력없음
@file.route("/aNot2Used")
def aNot2Used():
	if not 'no' in session:
		return redirect(url_for('login'))
	location = "files" + session['id']
	names, dates_edit = u.outDirList(location)
	return render_template('file_setting.html', names=names, dates_edit=dates_edit, use=u.outDirByte(location))

#해당 GID가 '사용하고 있는' 파일 a를 '사용하지 않는'으로 수정
#입력 {gid, 파일리스트} 출력없음
@file.route("/aUsed2Not")
def aUsed2Not():
	if not 'no' in session:
		return redirect(url_for('login'))
	location = "files" + session['id']
	names, dates_edit = u.outDirList(location)
	return render_template('file_setting.html', names=names, dates_edit=dates_edit, use=u.outDirByte(location))