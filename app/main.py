from app.database import SessionLocal
from app.models import StudentGrade


def main():
    db = SessionLocal()

    student = StudentGrade(
        last_name="Иванов",
        first_name="Иван",
        faculty="ФПМИ",
        subject="Мат. Анализ",
        grade=85
    )

    db.add(student)
    db.commit()
    db.close()

    print("Student added successfully!")


if __name__ == "__main__":
    main()