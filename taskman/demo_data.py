# набор задач для запуска с ключом --demo
from typing import List, Dict

Task = Dict[str, object]
TaskList = List[Task]


def get_demo_tasks() -> TaskList:
    return [
        {'id': 1, 'title': 'Аренда квартиры', 'priority': 45000, 'due': '2026-08-25', 'done': False},
        {'id': 2, 'title': 'Продукты', 'priority': 3200, 'due': '2026-09-01', 'done': False},
        {'id': 3, 'title': 'Проездной', 'priority': 2500, 'due': '2026-09-10', 'done': True},
        {'id': 4, 'title': 'Интернет', 'priority': 800, 'due': '2026-08-24', 'done': False},
        {'id': 5, 'title': 'Подписка на курс', 'priority': 1500, 'due': '2026-08-30', 'done': True},
        {'id': 6, 'title': 'Продукты на дачу', 'priority': 3200, 'due': '2026-09-05', 'done': False},
    ]
