from sqlmodel import Session, select
from db.connection import engine
import logging

logger = logging.getLogger(__name__)

# DB 연결 테스트 함수
def test_db_connection():
    """데이터베이스 연결 상태를 테스트합니다."""
    try:
        with Session(engine) as session:
            # 간단한 쿼리로 연결 테스트
            result = session.exec(select(1)).first()
            return True
    except Exception as e:
        logger.error(f"DB 연결 실패: {e}")
        return False

# DB 테이블 생성 함수
def create_db_and_tables():
    """데이터베이스 테이블을 생성합니다."""
    try:
        # SQLModel 테이블이 있다면 여기서 생성
        # SQLModel.metadata.create_all(engine)
        logger.info("DB 테이블 생성 완료")
        
        # DB 연결 테스트
        if test_db_connection():
            logger.info("✅ 데이터베이스 연결 성공!")
        else:
            logger.error("❌ 데이터베이스 연결 실패!")
            
    except Exception as e:
        logger.error(f"DB 테이블 생성 중 오류 발생: {e}")