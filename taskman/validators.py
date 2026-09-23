# проверки значений, каждая функция возвращает пару успех и ошибка
from typing import List, Tuple

max_length = 60

def validate_title(text: str):#проверить название задачи
    if not text:
        return False, 'название не может быть пустым'
    if len(text) > max_length:
        return False, f'название не должно быть длиннее {max_length} символов'
    return True

def validate_priority(value: int): #проверить приоритет задачи
    if not 1 <= value <= 5:
        return False, 'приоритет должен быть от 1 до 5'
    return True

def validate_due(text: str): #проверить срок в формате гггг-мм-дд
    if len(text) != 10:
        return False, 'срок должен быть в формате гггг-мм-дд'
    if text[4] != '-' or text[7] != '-':
        return False, 'срок должен быть в формате гггг-мм-дд'
    digits = text[0:4] + text[5:7] + text[8:10]
    if not digits.isdigit():
        return False, 'срок должен быть в формате гггг-мм-дд'
    month = int(text[5:7])
    if not 1 <= month <= 12:
        return False, 'срок должен быть в формате гггг-мм-дд'
    day = int(text[8:10])
    if not 1 <= day <= 31:
        return False, 'срок должен быть в формате гггг-мм-дд'
    return True

def validate_ident(value: int, idents: List[int]):#проверить что задача с таким идентификатором существует
    if value not in idents:
        return False, f'задачи с идентификатором {value} нет'
    return True



