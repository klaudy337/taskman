#диалог с пользователем и форматирование

def ask_text(prompt: str): #запросить строку у пользователя
    return input(prompt)


def ask_int(prompt: str, default): #запросить целое число и вернуть дефолт при пустом вводе
    text = input(prompt).strip()
    if text == '' and default is not None:
        return default
    if text:
        return text
    return None

def norm_title(text: str):#убрать лишние пробелы и сделать первую букву большой
    new_title = ' '.join(text.split())
    if not new_title:
        return new_title
    return new_title[0].upper() + new_title[1:]

def if_fragment(text: str, fragment: str): #проверить, содержит ли text фрагмент fragment без учёта регистра
    return fragment.lower() in text.lower()

def format_line(task, width: int = 25):#вернуть строку списка для одной задачи
    ident = task.get('id')
    priority = task.get('priority')
    title = str(task.get('title', ''))
    due = task.get('due')
    suffix = ' (выполнена)' if task.get('done') else ''
    return f'#{ident} [{priority}] {title:<{width}}| до {due}{suffix}'


