from pathlib import Path
from datetime import datetime
import re
from collections import Counter
import sys



def load_logs(file_path: str) -> list:
    path = Path(file_path)
    # Перевіряємо чи це файл
    if path.exists():
        with open(path, 'r', encoding='utf-8') as p:
            # Перевіряємо чи файл пустий
            lines = [line.strip() for line in p.readlines() if line.strip()]
            if lines:
                # Видаляємо всі пусті значення
                rare_list = [parse_log_line(x) for x in lines]
                return [i for i in rare_list if i != None]
            else:
                return None
    else:
        return None

 

# Розділяємо рядок на словник з перевіркою
def parse_log_line(line: str) -> dict:
    line_split = line.strip().split(' ')
    try:
        # Перевіряєм дату
        data = datetime.strptime(line_split[0], "%Y-%m-%d").date()
        time = datetime.strptime(line_split[1], "%H:%M:%S").time()
        # Перевіряєм тип логу
        type_log = line_split[2]
        
        return {"Data":data.strftime("%Y-%m-%d"),
                    "Time":time.strftime("%H:%M:%S"),
                    "Type":line_split[2],
                    "Text":' '.join(line_split[3:])}

    except ValueError:
        pass

# Створюємо словник який рахує кількість різних типів
def count_logs_by_level(logs: list) -> dict:
    try:
        return Counter(log["Type"] for log in logs)
    except TypeError:
        return "Невірний шлях"

# А це найцікавіше завдання) Цей скрипт малює табличку з словника 
def display_log_counts(counts: dict):
    # Прописуємо заголовок
    level_Log = 'Рівень логування'
    count = 'Кількість'
    header = f"{level_Log}|{count}"
    


    # Виводимо ключ і значення додаючи до ключа віступ і множимо його на вираз (довжина level_Log мінус довжина ключа)
    # Можна додати перевірку на довжину ключа і якщо вона більша за довжину level_Log додати ще відступ
    try:
        # Виводимо заголовок з застосуванням len()
        print(header)
        print(f'{"-"*len(level_Log)}|{"-"*len(count)}')

        for key, value in counts.items():
            print( f"{key}{' '*(len(level_Log) - len(key))}| {value}")
    except AttributeError:
        return print("Помилка атрибуту")

# Фільтруємо load_logs за ключем
def filter_logs_by_level(logs: list, level: str) -> list:

    log = [key for key in logs if key["Type"].upper() == level]
    # Перевіряємо чи введений лог правильно. Якщо ні то log пустий 
    if any(log):
        print(f"Деталі логів для рівня {level}:")
        for i in log:
            print(f'{i["Data"]} {i["Time"]} - {i["Text"]}')
    else:
        print("Невірно введена назва логу")


def main():
    # Приймаємо ввід з консолі 
    if len(sys.argv) == 2:
        user_path = load_logs(sys.argv[1])

        display_log_counts(count_logs_by_level(user_path))   
    elif len(sys.argv) == 3:
        user_level = sys.argv[2].upper()
        user_path = load_logs(Path(sys.argv[1])) 
        display_log_counts(count_logs_by_level(user_path))
        filter_logs_by_level(user_path,user_level)  
    else:
        return print("Невірно введені дані") 
    

if __name__ == "__main__":
    main()


