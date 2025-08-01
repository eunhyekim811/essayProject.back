from fastapi import APIRouter, HTTPException
from crud.dbtest import test_db_connection, create_db_and_tables

router = APIRouter(tags=["DB Test"])

# DB 연결 상태 확인 엔드포인트
@router.get("/health/db")
def check_db_health():
    """데이터베이스 연결 상태를 확인하는 헬스체크 엔드포인트"""
    if test_db_connection():
        return {
            "status": "healthy",
            "message": "데이터베이스 연결이 정상입니다",
            "database": "connected"
        }
    else:
        raise HTTPException(
            status_code=503,
            detail={
                "status": "unhealthy",
                "message": "데이터베이스 연결에 실패했습니다",
                "database": "disconnected"
            }
        )

# 전체 애플리케이션 상태 확인
@router.get("/health")
def health_check():
    """전체 애플리케이션 상태 확인"""
    db_status = test_db_connection()
    
    return {
        "status": "healthy" if db_status else "unhealthy",
        "services": {
            "database": "connected" if db_status else "disconnected",
            "api": "running"
        }
    }