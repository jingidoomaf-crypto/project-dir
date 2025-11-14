from datetime import date
from app import app
from models.db import db
from models.user_model import User
from werkzeug.security import generate_password_hash
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

def seed_data():
    with app.app_context():
        try:
            print("Starting database seeding")

            seed_users = [
                User(
                    fname="Jingi",
                    lname="Fortunato",
                    uname="Jingifortunato",
                    email="jhin@exapmle.com",
                    pass_word=generate_password_hash("jhin123"),
                    birthday=date(1999, 1, 1),
                    gender="Female",
                    phone_number="09130567789",
                    address="Pasig Street, Manila City",
                ), 
                User(
                    fname="Jovanie",
                    lname="Gador",
                    uname="jovaniegador",
                    email="jovaniegador@test.com",
                    pass_word=generate_password_hash("vanie123"),
                    birthday=date(2004, 13, 9),
                    gender="Male",
                    phone_number="09556648909",
                    address="Tondo Street, Manila City",
                )
            ]

            for user in seed_users:
                existing_user = User.querry.filter_by(email=user.email).first()
                if existing_user:
                    print(f"Skipping existing user: {user.email}")
                    continue
                db.session.add(user)
                db.session.commit()
                print("Database seeded successfully")

        except IntegrityError as e:
            db.session.rollback
            print(f"Integrity Error: {e}")

        except SQLAlchemyError as e:
            db.session.rollback
            print(f"SQLAlCHEMY Error: {e}")
        except Exception as e:
            db.session.rollback()
            print(f"Unexpected error seeding: {e}")

        finally:
            db.session.close()

if __name__ == "__main__":
    seed_data()