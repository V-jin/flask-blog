# app/routes.py
from app import app
from app.models import log_repo

@app.route("/")
def index():
    """API의 메인 소개 페이지를 렌더링합니다.

    Returns:
        str: 메인 페이지 환영 메시지 문자열.
    """
    return "Welcome to My Development Journal API"

@app.route("/home")
def home():
    """홈 페이지를 렌더링합니다.

    Returns:
        str: 홈 페이지 환영 메시지 문자열.
    """
    return "Welcome to the HOME page!"

@app.route("/course")
def course():
    """오픈소스 수업 테스트 페이지를 렌더링합니다.

    Returns:
        str: 오픈소스 수업 안내 문자열.
    """
    return "2026학년도 1학기 오픈소스 수업 테스트 페이지"

@app.route("/update")
def update():
    """모든 업데이트 내역을 웹 페이지에 출력합니다.

    LogRepository에서 모든 로그를 가져와 HTML 형태의 목록으로 변환한 뒤 반환합니다.

    Returns:
        str: 업데이트 내역이 포함된 완전한 HTML 문자열.
    """
    logs = log_repo.get_all()
    output = "<h1>업데이트 내역</h1>"
    output += "".join([log.to_html() for log in logs])
    return output

@app.route("/add/<date>/<content>")
def add_log_route(date, content):
    """새로운 업데이트 로그를 추가하는 API 엔드포인트입니다.

    URL 파라미터로 받은 날짜와 내용을 바탕으로 로그를 생성하고 저장소에 추가합니다.

    Args:
        date (str): 추가할 로그의 날짜 (URL 파라미터).
        content (str): 추가할 로그의 내용 (URL 파라미터).

    Returns:
        tuple: 로그 추가 성공 시 안내 HTML 문자열과 200 상태 코드,
               실패 시 에러 메시지와 400 상태 코드를 담은 튜플.

    ---
    
    tags:
      - Log API

    parameters:
      - name: date
        in: path
        type: string
        required: true
        description: 추가할 로그의 날짜 (eg. 2026-03-14)
      - name: content
        in: path
        type: string
        required: true
        description: 추가할 로그의 내용

    responses:
      200:
        description: 로그가 성공적으로 추가되었습니다.
      400:
        description: 날짜나 내용이 누락되어 실패했습니다.
    """
    if log_repo.add(date, content):
        return f"성공: {date} 내역이 추가되었습니다. <a href='/update'>확인하기</a>"
    return "실패: 날짜나 내용이 올바르지 않습니다.", 400