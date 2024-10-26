from app import db, create_app

app = create_app()

def reset_database():
    """Drop and recreate all tables in the database."""
    with app.app_context():
        db.drop_all()
        db.create_all()
        print("Database tables have been reset successfully.")
if __name__ == "__main__":
    reset_database()