# набор задач для запуска с ключом --demo
from typing import List, Dict

Task = Dict[str, object]
TaskList = List[Task]


def get_demo_tasks() -> TaskList:
    return [
        {'id': 1, 'title': 'Написать отчёт', 'priority': 5, 'due': '2026-08-25', 'done': False},
        {'id': 2, 'title': 'Купить хлеб', 'priority': 3, 'due': '2026-09-01', 'done': False},
        {'id': 3, 'title': 'Полить цветы', 'priority': 1, 'due': '2026-09-10', 'done': True},
        {'id': 4, 'title': 'Позвонить в банк', 'priority': 4, 'due': '2026-08-24', 'done': False},
        {'id': 5, 'title': 'Сдать блок', 'priority': 2, 'due': '2026-08-30', 'done': True},
        {'id': 6, 'title': 'Купить билеты', 'priority': 3, 'due': '2026-09-05', 'done': False},
    ]
