from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

#DATABASE_URL = "postgresql://username:password@localhost/resume_db"

DATABASE_URL = "postgresql://postgres:1234@localhost/resume_db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)



