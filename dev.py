from flask import Blueprint

from flask import make_response
from flask import request

dev = Blueprint('dev', __name__)

@dev.route("/register/<string:session_id>")
def send_cookie(session_id):
    content = f"session: {session_id}として登録しました"

    response = make_response(content)
    response.set_cookie('session_id', value=session_id)
    return response

@dev.route("/login_mitaina")
def get_cookie():
    session = request.cookies.get('session_id', None)

    if session == 'HogeHoge':
        content = "こんにちは、HogeHogeさん"
        # HogeHogeさん用の処理
    elif session == 'fuga':
        content = "こんにちは、fugaさん"
        # fugaさん用の処理
    else:
        content = "piyopiyo"
    return make_response(content)