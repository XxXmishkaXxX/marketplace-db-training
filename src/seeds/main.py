import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))
from faker import Faker 
from seeds.users import UserSeeder
from db.base import sync_session


faker = Faker("ru-RU")

def run_all() -> None:
    with sync_session() as session:
        seeder = UserSeeder(session=session, faker=faker)
        seeder.run_all(user_count=100,
                       addresses_per_user=2,
                       payment_methods_per_user=2,
                       sessions_per_user=1)


if __name__ == "__main__":
    run_all()