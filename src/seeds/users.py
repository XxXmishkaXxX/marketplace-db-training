import random
from faker import Faker
from sqlalchemy import select
from datetime import datetime, timedelta

from db.models import *



class UserSeeder:
    def __init__(self, session, faker: Faker | None = None):
        """
        :param session: активная SQLAlchemy сессия
        :param faker: объект Faker, если None — создаётся ru-RU
        """
        self.session = session
        self.faker = faker or Faker("ru-RU")

    def seed_roles(self):
        roles_list = ["user", "courier", "admin"]
        roles = [Role(name=role_name, description=self.faker.text()) for role_name in roles_list]
        self.session.add_all(roles)
        self.session.commit()

    def seed_users(self, count: int = 20):
        roles = {r.name: r for r in self.session.execute(select(Role)).scalars().all()}
        users = []

        for _ in range(count):
            user = User(
                name=self.faker.name(),
                email=self.faker.unique.email(),
                phone_number=self.faker.unique.phone_number(),
                password_hash=self.faker.password(),
                date_of_birth=self.faker.date_of_birth(),
            )
            # обязательная роль user
            user.roles.append(roles["user"])

            # рандомные дополнительные роли
            extra_roles = random.sample(
                [r for n, r in roles.items() if n != "user"],
                k=random.randint(0, len(roles) - 1)
            )
            user.roles.extend(extra_roles)

            users.append(user)

        self.session.add_all(users)
        self.session.commit()

    def seed_users_addresses(self, count_per_user: int = 2):
        users = self.session.execute(select(User)).scalars().all()
        user_addresses = []

        for user in users:
            for _ in range(count_per_user):
                user_addresses.append(
                    UserAddress(
                        user_id=user.id,
                        city=self.faker.city(),
                        street=self.faker.street_name(),
                        house_number=self.faker.building_number(),
                        apartment=f"кв. {random.randint(1, 200)}"
                    )
                )

        self.session.add_all(user_addresses)
        self.session.commit()

    def seed_users_wallets_and_payment_methods(self, count_per_user: int = 2):
        users = self.session.execute(select(User)).scalars().all()
        wallets = []
        payment_methods = []
        payment_types = ["card", "paypal", "apple_pay", "google_pay"]

        for user in users:
            # встроенный кошелёк
            wallet = Wallet(user_id=user.id, balance=0, currency="RUB")
            wallets.append(wallet)

            # способ оплаты "wallet"
            payment_methods.append(
                UserPaymentMethod(
                    user_id=user.id,
                    payment_type="wallet",
                    provider="Marketplace Wallet",
                    account_number_masked=f"WALLET-{user.id}",
                    expiration_date=None,
                    is_default=True
                )
            )

            # дополнительные методы
            for _ in range(count_per_user):
                p_type = random.choice(payment_types)
                if p_type == "card":
                    card_number = self.faker.credit_card_number()
                    account_number_masked = f"**** **** **** {card_number[-4:]}"
                    provider = self.faker.credit_card_provider()
                    expiration_date = self.faker.credit_card_expire(date_format="%m/%y")
                else:
                    account_number_masked = self.faker.uuid4()[:8]
                    provider = p_type.replace("_", " ").title()
                    expiration_date = None

                payment_methods.append(
                    UserPaymentMethod(
                        user_id=user.id,
                        payment_type=p_type,
                        provider=provider,
                        account_number_masked=account_number_masked,
                        expiration_date=expiration_date,
                        is_default=False
                    )
                )

        self.session.add_all(wallets)
        self.session.add_all(payment_methods)
        self.session.commit()

    def seed_users_sessions(self, sessions_per_user: int = 2):
        users = self.session.execute(select(User)).scalars().all()
        sessions_data = []

        for user in users:
            for _ in range(sessions_per_user):
                token_plain, token_hash = UserSession.generate_token()
                created_at = self.faker.date_time_this_year()
                expires_at = created_at + timedelta(days=random.randint(1, 30))

                sessions_data.append(
                    UserSession(
                        user_id=user.id,
                        token_hash=token_hash,
                        device_info=self.faker.user_agent()[:128],
                        ip_address=self.faker.ipv4_public(),
                        expires_at=expires_at,
                    )
                )

        self.session.add_all(sessions_data)
        self.session.commit()

    def run_all(self, user_count: int = 20, addresses_per_user: int = 2,
                payment_methods_per_user: int = 2, sessions_per_user: int = 2):
        """Запуск всех сидеров в правильном порядке"""
        self.seed_roles()
        self.seed_users(user_count)
        self.seed_users_addresses(addresses_per_user)
        self.seed_users_wallets_and_payment_methods(payment_methods_per_user)
        self.seed_users_sessions(sessions_per_user)