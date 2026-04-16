from sqlalchemy import Column, Integer, String
from .database import Base


class StudentGrade(Base):
    __tablename__ = "student_grades"

    id = Column(Integer, primary_key=True, index=True)

    last_name = Column(String, nullable=False)
    first_name = Column(String, nullable=False)
    faculty = Column(String, nullable=False)
    subject = Column(String, nullable=False)
    grade = Column(Integer, nullable=False)