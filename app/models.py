# app/models.py
import os

class UpdateLog:
    """업데이트 로그 데이터를 담는 클래스입니다.

    Attributes:
        date (str): 업데이트 날짜 (예: '2026-03-13')
        content (str): 업데이트 상세 내용
    """
    def __init__(self, date: str, content: str):
        """UpdateLog 인스턴스를 초기화합니다.

        Args:
            date (str): 로그의 날짜.
            content (str): 로그의 내용.

        Raises:
            ValueError: 날짜나 내용이 비어있을 경우 발생합니다.
        """
        if not date or not content:
            raise ValueError("날짜와 내용은 필수입니다.")
        self.date = date
        self.content = content

    def to_html(self):
        """로그 데이터를 HTML 단락(p 태그) 형태로 변환하여 반환합니다.
        
        Returns:
            str: 포맷팅된 HTML 문자열 (예: '<p>날짜 - 내용</p>').
        """
        return f"<p>{self.date} - {self.content}</p>"


class LogRepository:
    """로그 데이터를 텍스트 파일(txt) 기반으로 영구 보관하는 레포지토리 클래스입니다."""

    def __init__(self, filepath="logs.txt"):
        """LogRepository 인스턴스를 초기화하고 파일에서 기존 로그를 불러옵니다.

        Args:
            filepath (str): 로그를 저장할 텍스트 파일의 경로. 기본값은 'logs.txt'입니다.
        """
        self.filepath = filepath
        self._db = []
        self._load_from_file()

    def _load_from_file(self):
        """텍스트 파일에서 기존 로그 데이터를 읽어와 메모리(_db)에 적재합니다."""
        if not os.path.exists(self.filepath):
            # 파일이 없으면 뼈대가 되는 기본 로그 하나를 파일에 쓰고 시작합니다.
            self.add("2026-03-13", "기초 Flask 웹 서버 설정 완료")
            return

        # 파일이 존재하면 읽기 모드('r')로 엽니다.
        with open(self.filepath, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()  # 줄바꿈 문자(\n) 제거
                if line:
                    # '날짜|내용' 형태의 텍스트를 분리해서 객체로 만듭니다.
                    parts = line.split('|', 1)
                    if len(parts) == 2:
                        date, content = parts
                        self._db.append(UpdateLog(date, content))

    def get_all(self):
        """저장소에 보관된 모든 업데이트 로그를 반환합니다.

        Returns:
            list: UpdateLog 객체들이 담긴 리스트.
        """
        return self._db

    def add(self, date: str, content: str):
        """새로운 업데이트 로그를 파일에 추가하고 메모리에도 반영합니다.

        Args:
            date (str): 추가할 로그의 날짜.
            content (str): 추가할 로그의 내용.

        Returns:
            bool: 로그가 성공적으로 추가되었으면 True, 값 오류로 실패하면 False.
        """
        try:
            new_log = UpdateLog(date, content)
            self._db.append(new_log) # 메모리에 먼저 추가
            
            # 파일에도 내용 추가 (추가 모드 'a')
            with open(self.filepath, 'a', encoding='utf-8') as f:
                f.write(f"{date}|{content}\n")
                
            return True
        except ValueError:
            return False

# 의존성 주입을 위한 인스턴스 생성
log_repo = LogRepository()