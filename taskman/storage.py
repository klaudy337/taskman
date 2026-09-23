# операции над списком задач, модуль ничего не печатает и не запрашивает ввод
from typing import List, Dict, Optional
from operator import itemgetter

Task = Dict[str, object]
TaskList = List[Task]

# названия категорий приоритета
labels: Dict[int, str] = {
    5: 'критическая',
    4: 'срочная',
    3: 'обычная',
    2: 'обычная',
    1: 'фоновая',
}


def make_task(title: str, priority: int, due: str, done: bool = False):#собрать задачу без идентификатора
    return {'title': title, 'priority': priority, 'due': due, 'done': done}


def next_ident(tasks: TaskList):#вернуть идентификатор для новой задачи
    idents = [task.get('id', 0) for task in tasks]
    return max(idents) + 1 if idents else 1


def add_task(tasks: TaskList, task: Task):#добавить задачу в список, присвоив ей идентификатор
    task['id'] = next_ident(tasks)
    tasks.append(task)
    return task


def find_by_ident(tasks: TaskList, ident: int):#вернуть задачу по идентификатору или None если такой нет
    for task in tasks:
        if task.get('id') == ident:
            return task
    return None


def remove_by_ident(tasks: TaskList, ident: int):# удалить задачу по идентификатору и вернуть признак успеха
    task = find_by_ident(tasks, ident)
    if task is None:
        return False
    tasks.remove(task)
    return True


def mark_done(tasks: TaskList, ident: int):#отметить задачу выполненной по идентификатору, вернуть признак успеха
    task = find_by_ident(tasks, ident)
    if task is None:
        return False
    task['done'] = True
    return True


def filter_tasks(
    tasks: TaskList, done: Optional[bool] = None, min_priority: Optional[int] = None):#вернуть новый список задач, подходящих под заданные условия
    result = list(tasks)
    if done is not None:
        result = [task for task in result if task.get('done') == done]
    if min_priority is not None:
        result = [task for task in result if task.get('priority', 0) >= min_priority]
    return result


def sort_tasks(tasks: TaskList, key: str = 'priority', reverse: bool = True):#вернуть новый список задач, отсортированный по указанному ключу
    return sorted(tasks, key=itemgetter(key), reverse=reverse)


def stats(tasks: TaskList):#вернуть статистику: всего, выполнено, осталось, средний приоритет невыполненных
    total = len(tasks)
    done_count = sum(1 for task in tasks if task.get('done'))
    left = total - done_count
    active = [task for task in tasks if not task.get('done')]
    avg_priority = sum(task.get('priority', 0) for task in active) / len(active) if active else 0.0
    return {'total': total, 'done': done_count, 'left': left, 'avg_priority': avg_priority}


