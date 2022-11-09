from flask import Blueprint, session, redirect, url_for, render_template
database = Blueprint("database", __name__, url_prefix="/database")
#데이터베이스와 소통하는 api

