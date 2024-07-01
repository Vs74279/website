

from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    firstName = Column(String)
    lastName = Column(String)
    phone = Column(String)
    email = Column(String)
 
class JobApplication(Base):
    __tablename__ = "job_applications"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), unique=True)
    user = relationship("User", back_populates="job_applications")
    job_title = Column(String)
    job_description = Column(Text)
    fullName = Column(String)
    phone = Column(String)
    email = Column(String)
    upload_file = Column(String)
    photo = Column(String)
    address = Column(Text)
    position = Column(String)
    gender = Column(String)
    qualification = Column(String)
    reference = Column(Text)
    application_date = Column(DateTime, default=datetime.utcnow)

User.job_applications = relationship("JobApplication", back_populates="user")
