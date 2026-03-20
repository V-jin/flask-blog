#app.py

from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Welcome to My Development Journal API"

@app.route("/home")
def home():
    return "Welcome to the HOME page!"

@app.route("/course")
def course():
    return "2026학년도 1학기 오픈소스 수업 테스트 페이지"

#260320 추가 - 기능 업뎃내역
@app.route("/update")
def update():
    logs = get_all_updates()

    output = "<h1>업데이트 내역</h1>"
    for log in logs:
        output += f"<p>{log['date']} - {log['content']}</p>"
        
    return output

INITIAL_LOG = {"date": "2026-03-13", "content": "기초 Flask 웹 서버 설정 완료"}
updates_db = [INITIAL_LOG]
def get_all_updates():
    """
    모든 업데이트 내역 리스트를 반환함
    반환 형식: [{"date": "YYYY-MM-DD", "content": "..."}, ...]
    """
    return updates_db

def add_update_log(date, content):
    """
    새로운 업데이트 내역을 추가함
    성공 시 True, 데이터가 누락되면 False를 반환함
    """
    # 1. 유효성 검사: 날짜나 내용이 없으면 실패 처리
    if not _is_valid_input(date, content):
        return False
    
    # 2. 새로운 로그 객체 생성 및 추가
    updates_db.append({"date": date, "content": content})    
    return True

def _is_valid_input(date, content):
    return bool(date and content)

#실시간 로그 추가 기능 (Web Route) 260320
@app.route("/add/<date>/<content>")
def add_log_route(date, content):
    if add_update_log(date, content):
        return f"성공: {date} 내역이 추가되었습니다. <a href='/update'>확인하기</a>"
    else:
        return "실패: 날짜나 내용이 올바르지 않습니다.", 400
    
#저장도 되면 좋겠는데 그건 .txt나 log파일을 만들어야 한다
    
if __name__ == "__main__":
    app.run(host = "0.0.0.0", port=5000, debug=True)

