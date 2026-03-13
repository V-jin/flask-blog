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

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port=5000, debug=True)