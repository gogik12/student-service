# student-service

Небольшой учебный сервис для работы со списком студентов: загрузка из json,
добавление записи, выборка по группе.

## Запуск

```bash
python -c "import students; print(students.by_group(students.load(), 'ОВБИ-304б'))"
```

## Тесты

```bash
pip install pytest
pytest -q
```
