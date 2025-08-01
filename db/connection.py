from config import settings
from sqlmodel import create_engine

db_url = settings.DB_URL

engine = create_engine(db_url)