import pytest
from app import get_all_updates, add_update_log, updates_db

# 테스트를 실행할 때마다 DB(리스트)를 초기화하는 장치야.
@pytest.fixture(autouse=True)
def setup_db():
    updates_db.clear()
    updates_db.append({"date": "2026-03-19", "content": "기초 Flask 웹 서버 설정 완료"})

# 1. 초기 데이터 조회 테스트
def test_get_all_updates_should_return_initial_data():
    # When: 모든 업데이트 내역을 가져왔을 때
    results = get_all_updates()
    
    # Then: 처음에 넣은 데이터 1개가 들어있어야 함
    assert isinstance(results, list)
    assert len(results) == 1
    assert results[0]["content"] == "기초 Flask 웹 서버 설정 완료"

# 2. 새로운 내역 추가 성공 테스트 (Happy Path)
def test_add_update_log_success():
    # Given: 새로운 날짜와 내용
    date = "2026-03-20"
    content = "TADD 실습 시작"
    
    # When: 데이터를 추가했을 때
    result = add_update_log(date, content)
    
    # Then: 결과는 True여야 하고, 전체 개수가 2개가 되어야 함
    assert result is True
    assert len(get_all_updates()) == 2
    assert get_all_updates()[1]["date"] == "2026-03-20"

# 3. 데이터 누락 시 실패 테스트 (Edge Case)
def test_add_update_log_fail_due_to_empty_data():
    # When: 내용(content) 없이 추가를 시도했을 때
    result = add_update_log("2026-03-20", "")
    
    # Then: 결과는 False여야 함
    assert result is False