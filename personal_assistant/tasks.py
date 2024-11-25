import json
import csv

class TasksManager:
    FILE_NAME = "tasks.json"

    def __init__(self):
        self.tasks = self.load_tasks()

    def load_tasks(self):
        try:
            with open(self.FILE_NAME, 'r', encoding='utf-8') as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def save_tasks(self):
        with open(self.FILE_NAME, 'w', encoding='utf-8') as file:
            json.dump(self.tasks, file, ensure_ascii=False, indent=4)

    def add_task(self):
        title = input("Введите краткое описание задачи: ")
        description = input("Введите подробное описание задачи: ")
        priority = input("Введите приоритет (Высокий, Средний, Низкий): ")
        due_date = input("Введите срок выполнения (ДД-ММ-ГГГГ): ")
        task = {
            "id": len(self.tasks) + 1,
            "title": title,
            "description": description,
            "done": False,
            "priority": priority,
            "due_date": due_date
        }
        self.tasks.append(task)
        self.save_tasks()
        print("Задача добавлена.")

    def view_tasks(self, filter_by_status=None):
        if not self.tasks:
            print("Список задач пуст.")
            return

        filtered_tasks = self.tasks
        if filter_by_status is not None:
            filtered_tasks = [task for task in self.tasks if task["done"] == filter_by_status]

        for task in filtered_tasks:
            status = "Выполнено" if task["done"] else "Не выполнено"
            print(
                f"[{task['id']}] {task['title']} | Статус: {status} | Приоритет: {task['priority']} | Срок: {task['due_date']}")

    def mark_as_done(self):
        self.view_tasks(filter_by_status=False)
        try:
            task_id = int(input("Введите ID выполненной задачи: "))
            task = next((t for t in self.tasks if t["id"] == task_id), None)
            if task:
                task["done"] = True
                self.save_tasks()
                print("Задача отмечена как выполненная.")
            else:
                print("Задача не найдена.")
        except ValueError:
            print("Неверный ввод.")

    def edit_task(self):
        self.view_tasks()
        try:
            task_id = int(input("Введите ID задачи для редактирования: "))
            task = next((t for t in self.tasks if t["id"] == task_id), None)
            if task:
                task["title"] = input("Введите новое краткое описание: ") or task["title"]
                task["description"] = input("Введите новое описание: ") or task["description"]
                task["priority"] = input("Введите новый приоритет: ") or task["priority"]
                task["due_date"] = input("Введите новый срок выполнения (ДД-ММ-ГГГГ): ") or task["due_date"]
                self.save_tasks()
                print("Задача обновлена.")
            else:
                print("Задача не найдена.")
        except ValueError:
            print("Неверный ввод.")

    def delete_task(self):
        self.view_tasks()
        try:
            task_id = int(input("Введите ID задачи для удаления: "))
            self.tasks = [t for t in self.tasks if t["id"] != task_id]
            self.save_tasks()
            print("Задача удалена.")
        except ValueError:
            print("Неверный ввод.")

    def export_to_csv(self):
        filename = input("Введите имя файла для экспорта (например, tasks.csv): ")
        with open(filename, 'w', encoding='utf-8', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=["id", "title", "description", "done", "priority", "due_date"])
            writer.writeheader()
            writer.writerows(self.tasks)
        print(f"Задачи экспортированы в файл {filename}.")

    def import_from_csv(self):
        filename = input("Введите имя файла для импорта (например, tasks.csv): ")
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    row["id"] = int(row["id"])
                    row["done"] = row["done"].lower() == "true"
                    self.tasks.append(row)
                self.save_tasks()
            print(f"Задачи импортированы из файла {filename}.")
        except FileNotFoundError:
            print("Файл не найден.")

    def menu(self):
        while True:
            print("\nУправление задачами:")
            print("1. Добавить задачу")
            print("2. Просмотреть список задач")
            print("3. Отметить задачу как выполненную")
            print("4. Редактировать задачу")
            print("5. Удалить задачу")
            print("6. Экспортировать в CSV")
            print("7. Импортировать из CSV")
            print("8. Вернуться в главное меню")

            choice = input("Выберите действие: ")
            if choice == "1":
                self.add_task()
            elif choice == "2":
                self.view_tasks()
            elif choice == "3":
                self.mark_as_done()
            elif choice == "4":
                self.edit_task()
            elif choice == "5":
                self.delete_task()
            elif choice == "6":
                self.export_to_csv()
            elif choice == "7":
                self.import_from_csv()
            elif choice == "8":
                break
            else:
                print("Неверный ввод. Попробуйте снова.")