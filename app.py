from flask import Flask, render_template_string
from abc import ABC, abstractmethod

app = Flask(__name__)

# 로그 업데이트
class UpdateLog:
    def __init__(self, date: str, content: str):
        if not date or not content:
            raise ValueError("날짜와 내용은 필수입니다.")
        self.date = date
        self.content = content

    def to_html(self):
        return f"<p>{self.date} - {self.content}</p>"

# 로그 데이터 관리
class LogRepository:
    def __init__(self):
        self._db = [UpdateLog("2026-03-13", "기초 Flask 웹 서버 설정 완료")]

    def get_all(self):
        return self._db

    def add(self, date, content):
        try:
            new_log = UpdateLog(date, content)
            self._db.append(new_log)
            return True
        except ValueError:
            return False

# 의존성 주입을 위한 인스턴스 생성 (DIP 원칙 활용 가능성 확보)
log_repo = LogRepository()

# 홈피 요청 처리
@app.route("/")
def index():
    return "Welcome to My Development Journal API"

@app.route("/home")
def home():
    return "Welcome to the HOME page!"

@app.route("/course")
def course():
    return "2026학년도 1학기 오픈소스 수업 테스트 페이지"

@app.route("/update")
def update():
    logs = log_repo.get_all()
    output = "<h1>업데이트 내역</h1>"
    output += "".join([log.to_html() for log in logs])
    return output

@app.route("/add/<date>/<content>")
def add_log_route(date, content):
    if log_repo.add(date, content):
        return f"성공: {date} 내역이 추가되었습니다. <a href='/update'>확인하기</a>"
    return "실패: 날짜나 내용이 올바르지 않습니다.", 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)