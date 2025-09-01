# Marketplace DB — SQLAlchemy ORM

Масштабная учебная БД маркетплейса уровня «мультивендор»: пользователи, роли, товары, заказы, логистика, финансы, маркетинг, поддержка, подписки, интеграции. Репозиторий предназначен для тренировки SQLAlchemy ORM (Declarative), миграций Alembic и написания запросов.

---

## 1) Фичи
- Полный набор связей: 1:1, 1:N, M:N, self-relation, M:N с атрибутами
- Модели разбиты по доменам: users, catalog, orders, warehouse, finance
- Alembic миграции и сидер с Faker
- Примеры запросов ORM: фильтры, join, selectinload, subqueryload, агрегаты, транзакции
- Docker Compose с PostgreSQL

---
