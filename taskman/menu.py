#цикл главного меню
from . import io_utils
from . import storage
Task = storage.Task
TaskList = storage.TaskList

menutext = ('1 - добавить, 2 - список, 3 - открыть, 4 - выполнить, 5 - удалить, '
             '6 - статистика, 7 - поиск, 0 - выход')

def title_ask():#запросить и вернуть проверенное название задачи
    while True:
        raw = io_utils.ask_text('название: ')
        title = io_utils.norm_title(raw)
        return title

def priority_ask(): #запросить и вернуть проверенный приоритет задачи
    while True:
        raw = io_utils.ask_int('число: ')
        if raw is None:
            print('ошибка: нужно целое число')
            continue
        return raw

def due_ask():#запросить и вернуть проверенный срок задачи
    while True:
        raw = io_utils.ask_text('дата: ')
        return raw

def ident_ask(tasks: TaskList, prompt: str = 'идентификатор: '):#запросить и вернуть идентификатор существующей задачи
    idents = [task['id'] for task in tasks]
    while True:
        raw = io_utils.ask_text(prompt).strip()
        
        value = int(raw)
        return value

def card_print(task: Task):#напечатать подробную карточку задачи
    priority = task.get('priority')
    # label = storage.labels.get(priority, '')
    status = 'оплачен' if task.get('done') else 'не оплачен'
    print(f'расход #{task.get('id')}')
    print(f'описание: {task.get('title')}')
    print(f'сумма: {priority}')
    print(f'дата: {task.get('due')}')
    print(f'статус: {status}')
    

def cmd_add(tasks: TaskList):#добавить новую задачу
    title = title_ask()
    priority = priority_ask()
    due = due_ask()
    task = storage.make_task(title, priority, due)
    storage.add_task(tasks, task)
    print(f'расход #{task['id']} добавлен')

def cmd_list(tasks: TaskList):#показать список задач
    if not tasks:
        print('расходов нет')
        return
    for task in tasks:
        print(io_utils.format_line(task))

def cmd_open(tasks: TaskList):#открыть подробную карточку задачи по идентификатору
    if not tasks:
        print('расходов нет')
        return
    ident = ident_ask(tasks)
    task = storage.find_by_ident(tasks, ident)
    card_print(task)

def cmd_done(tasks: TaskList):#отметить задачу выполненной по идентификатору
    if not tasks:
        print('расходов нет')
        return
    ident = ident_ask(tasks)
    storage.mark_done(tasks, ident)
    task = storage.find_by_ident(tasks, ident)
    print(f"расход '{task['title']}' оплачен")

def cmd_remove(tasks: TaskList):#удалить задачу по идентификатору
    if not tasks:
        print('задач нет')
        return
    ident = ident_ask(tasks)
    task = storage.find_by_ident(tasks, ident)
    title = task['title']
    storage.remove_by_ident(tasks, ident)
    print(f"расход '{title}' удален")

def cmd_stats(tasks: TaskList): #показать статистику по расходам
    data = storage.stats(tasks)
    print(f'всего: {data["total"]}, оплачено: {data["done"]}, '
          f'неоплачено: {data["left"]}, средняя сумма: {data["avg_priority"]:.1f}')

def cmd_search(tasks: TaskList): #найти задачи по фрагменту названия или по идентификатору
    raw = io_utils.ask_text('фрагмент или id: ').strip()
    found = [task for task in tasks if io_utils.if_fragment(str(task.get('title', '')), raw)]
    if not found:
        print('ничего не найдено')
        return
    for task in found:
        print(io_utils.format_line(task))
    print(f'найдено: {len(found)}')


def run(tasks): #запустить цикл главного меню
    if tasks is None:
        tasks = []
    print(menutext)
    while True:
        command = input('> ').strip()
        if command == '':
            continue
        if command == '1':
            cmd_add(tasks)
        elif command == '2':
            cmd_list(tasks)
        elif command == '3':
            cmd_open(tasks)
        elif command == '4':
            cmd_done(tasks)
        elif command == '5':
            cmd_remove(tasks)
        elif command == '6':
            cmd_stats(tasks)
        elif command == '7':
            cmd_search(tasks)
        elif command == '0':
            print('выход...')
            break
        else:
            print('неизвестная команда')


