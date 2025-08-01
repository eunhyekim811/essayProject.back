from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlmodel import Session, select
from db.connection import engine
import logging
from routers.dbtest import router as dbtest_router
from crud.dbtest import create_db_and_tables

# 로깅 설정
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

# CORS 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,  # 쿠키 허용
    allow_methods=["GET", "POST"],
    allow_headers=["*"],  # 모든 요청 헤더 허용
)

# 앱 시작 시 DB 테이블 생성
@app.on_event("startup")
def on_startup():
    create_db_and_tables()

app.include_router(dbtest_router)