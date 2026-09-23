#запустить приложение и обработать ключи командной строки
import sys
from typing import List
from .menu import run as run_menu
from .demo_data import get_demo_tasks

helptext = (
    'Менеджер личных задач.\n'
    'Использование: python -m taskman \n'
    '  --demo   запустить с демонстрационным набором задач\n'
    '  --help   показать эту справку'
)


def run(): #запустить приложение
    args = sys.argv[1:]
    if '--help' in args:
        print(helptext)
        return
    tasks: List = get_demo_tasks() if '--demo' in args else []
    run_menu(tasks)


if __name__ == '__main__':
    run()
