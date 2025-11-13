from app import app
from models.db import db
from models.user import User
from werkzeug.security import generate_password_hash
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

def seed_data():
    with app.app_context():
        try:
            print("Starting database seeding...")

            # List of users to seed
            seed_users = [
                User(
                    fname="Sofia",
                    lname="Mendez",
                    uname="sofia",
                    email="ssofiamendez98@example.com",
                    pass_word=generate_password_hash("sofia143")
                ),
                User(
                    fname="Kween",
                    lname="Yasmin",
                    uname="kween",
                    email="kweentheogsierramadre25@test.com",  # Fixed typo
                    pass_word=generate_password_hash("kween123")
                )
            ]

            # Add users if they don't already exist
            for user in seed_users:
                existing_user = User.query.filter_by(email=user.email).first()
                if existing_user:
                    print(f"Skipping existing user: {user.email}")
                    continue
                db.session.add(user)
                print(f"Added user: {user.email}")

            # Commit all changes
            db.session.commit()
            print("Database seeded successfully!")

        except IntegrityError as e:
            db.session.rollback()
            print(f"Integrity error: {e}")

        except SQLAlchemyError as e:
            db.session.rollback()
            print(f"SQLAlchemy error: {e}")

        except Exception as e:
            db.session.rollback()
            print(f"Unexpected error during seeding: {e}")

        finally:
            db.session.close()
            print("Seeding process finished.")

if __name__ == '__main__':
    seed_data()