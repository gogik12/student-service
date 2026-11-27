"""Работа со списком студентов: загрузка, добавление, поиск по группе."""

import json
import re
from pathlib import Path

DATA = Path(__file__).with_name("data") / "students.json"

EMAIL_RE = re.compile(r"^[^@\s]+@[^@\s]+\.[A-Za-zА-Яа-я]{2,}$")


def load(path: Path = DATA) -> list[dict]:
    """Читает список студентов из json-файла."""
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


def save(items: list[dict], path: Path = DATA) -> None:
    """Записывает список студентов в json-файл."""
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(items, fh, ensure_ascii=False, indent=2)


def validate_email(value: str) -> bool:
    """Проверяет формат адреса электронной почты.

    Простая проверка без внешних зависимостей: одна «собака», домен с точкой
    и доменной зоной не короче двух букв; в локальной части точки не стоят
    в начале, в конце и не идут подряд.
    """
    address = (value or "").strip()
    if not EMAIL_RE.match(address):
        return False
    local = address.split("@", 1)[0]
    return not (local.startswith(".") or local.endswith(".") or ".." in local)


def add(items: list[dict], name: str, group: str, email: str = "") -> dict:
    """Добавляет студента в список и возвращает добавленную запись.

    Если email передан, он проверяется: некорректный адрес даёт ValueError.
    """
    if email and not validate_email(email):
        raise ValueError(f"Некорректный адрес электронной почты: {email}")
    record = {"name": name.strip(), "group": group.strip()}
    if email:
        record["email"] = email.strip().lower()
    items.append(record)
    return record


def by_group(items: list[dict], group: str) -> list[dict]:
    """Возвращает студентов указанной группы."""
    return [item for item in items if item["group"] == group]
