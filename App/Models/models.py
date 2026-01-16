from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Text

Base = declarative_base()

class Resume(Base):
    __tablename__ = "resumes"

    id = Column(Integer, primary_key=True)
    full_name = Column(String(100))
    email = Column(String(100))
    phone = Column(String(20))
    skills = Column(Text)
    education = Column(Text)
    experience = Column(Text)

