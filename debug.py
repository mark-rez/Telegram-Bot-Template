from database import SessionLocal
from models import User

session = SessionLocal()

users = session.query(User).all()

print("=== Users in DB ===")
for user in users:
    user_data = user.__dict__ 
    for attr, value in reversed(user_data.items()):
        if not attr.startswith('_'):
            print(f"{attr}: {value}, ", end="")
    print()

session.close()
