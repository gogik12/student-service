# student-service

Небольшой учебный сервис для работы со списком студентов: загрузка из json,
добавление записи, выборка по группе.

## Запуск

```bash
python -c "import students; print(students.by_group(students.load(), 'ОВБИ-304б'))"
```

## Проверка email

При добавлении студента можно передать адрес почты — он проверяется по формату,
хранится в нижнем регистре и попадает в запись как поле `email`.

```python
students.add(items, "Иванов Иван", "ОВБИ-304б", "Ivanov@Example.RU")
# {'name': 'Иванов Иван', 'group': 'ОВБИ-304б', 'email': 'ivanov@example.ru'}
```

Некорректный адрес даёт `ValueError`.

## Тесты

```bash
pip install pytest
pytest -q
```
