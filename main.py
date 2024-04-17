"""
Создай класс `Task`, который позволяет управлять задачами (делами).
У задачи должны быть атрибуты: описание задачи, срок выполнения и
статус (выполнено/не выполнено). Реализуй функцию для добавления
задач, отметки выполненных задач и вывода списка текущих
(не выполненных) задач.
"""


class Task:
    def __init__(self, description, due_date):
        self.description = description
        self.due_date = due_date
        self.completed = False

    def mark_as_completed(self):
        self.completed = True


tasks = []  # Список задач


# Функция добавления задачи
def add_task(description, due_date):
    tasks.append(Task(description, due_date))


# Функция отметки выполнения задачи по имени задачи
def mark_task_completed(done_task):
    for t in tasks:
        if t.description == done_task:
            t.mark_as_completed()
            break


# Функция вывода списка текущих задач
def print_tasks_completed():
    print("Текущие задачи:")
    for t in tasks:
        if not t.completed:
            print(f"{t.description} надо выполнить до {t.due_date}")


print("Создаем задачи 1 - 4:")
tasks.append(Task("Задача 1", "20.05.2024"))
tasks.append(Task("Задача 2", "02.05.2024"))
tasks.append(Task("Задача 3", "22.05.2024"))
tasks.append(Task("Задача 4", "12.05.2024"))
print_tasks_completed()  # список текущих задач

mark_task_completed("Задача 2")  # Задача 2 выполнена
mark_task_completed("Задача 4")  # Задача42 выполнена
print("\n После выполнения задач 2, 4 выводим список текущих задач:")
print_tasks_completed()  # список текущих задач




