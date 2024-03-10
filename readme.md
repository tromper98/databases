# Развертывание demo базы
1. Копировать базу в docker-контейнер:
```bash
docker cp ./scripts/demo-medium-20170815.sql docker_postgres-db_1:/
```
2. Зайти в docker-контейнер
```bash
docker exec -it docker_postgres-db_1 bash
```
3. Выполнить развертывания БД из дампа:
```bash
psql -f demo-medium-20170815.sql  -U admin -d postgres
```