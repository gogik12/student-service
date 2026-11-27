"""Работа со списком студентов: загрузка, добавление, поиск по группе."""

import json
from pathlib import Path

DATA = Path(__file__).with_name("data") / "students.json"


def load(path: Path = DATA) -> list[dict]:
    """Читает список студентов из json-файла."""
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


def save(items: list[dict], path: Path = DATA) -> None:
    """Записывает список студентов в json-файл."""
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(items, fh, ensure_ascii=False, indent=2)


def add(items: list[dict], name: str, group: str) -> dict:
    """Добавляет студента в список и возвращает добавленную запись."""
    record = {"name": name.strip(), "group": group.strip()}
    items.append(record)
    return record


def by_group(items: list[dict], group: str) -> list[dict]:
    """Возвращает студентов указанной группы."""
    return [item for item in items if item["group"] == group]
