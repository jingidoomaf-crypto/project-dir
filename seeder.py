from app import app
from models.db import db
from models.user_model import User
from werkzeug.security import generate_password_hash
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from datetime import date

def seed_data():
    with app.app_context():
        try:
            print("Starting database seeding")

            seed_users = [
                User(
                    fname="Maria",
                    lname="Clara",
                    email="mariaclara@example.com",
                    pass_word=generate_password_hash("maria123"),
                    birthday=date(1990, 1, 1),
                    gender="Female",
                    phone_number="09171234567",
                    address="Rizal Street, Manila City",
                    student_id="STU026"
                ),
                User(
                    fname="Juan",
                    lname="Tamad",
                    email="juantamad@test.com",
                    pass_word=generate_password_hash("juantamad123"),
                    birthday=date(2000, 5, 15),
                    gender="Male",
                    phone_number="09179876543",
                    address="123 Dormitory, Manila",
                    student_id="STU030"
                )
            ]

            for user in seed_users:
                existing_user = User.query.filter_by(email=user.email).first()
                if existing_user:
                    print(f"Skipping existing user: {user.email}")
                    continue
                db.session.add(user)

            db.session.commit()
            print("Database seeded successfully")

        except IntegrityError as e:
            db.session.rollback()
            print(f"Integrity error: {e}")

        except SQLAlchemyError as e:
            db.session.rollback()
            print(f"SQLALCHEMY error: {e}")

        except Exception as e:
            db.session.rollback()
            print(f"Unexpected error during seeding: {e}")

        finally:
            db.session.close()


if __name__ == "__main__":
    seed_data()
