import students


def test_validate_email_accepts_normal_address():
    assert students.validate_email("ivanov@example.ru")


def test_validate_email_rejects_broken_address():
    for bad in ["", "ivanov", "ivanov@", "ivanov@example", "ivanov example@mail.ru"]:
        assert not students.validate_email(bad)


def test_validate_email_rejects_dot_edges_and_double_dots():
    for bad in ["ivanov..petrov@mail.ru", "ivanov.@mail.ru", ".ivanov@mail.ru"]:
        assert not students.validate_email(bad)


def test_add_stores_lowercase_email():
    items = []
    record = students.add(items, "Иванов Иван", "ОВБИ-304б", "Ivanov@Example.RU")
    assert record["email"] == "ivanov@example.ru"
    assert items == [record]


def test_add_without_email_keeps_old_format():
    items = []
    record = students.add(items, "Петрова Анна", "ОВБИ-304б")
    assert "email" not in record
