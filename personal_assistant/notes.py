import json
import csv
from datetime import datetime

class NotesManager:
    FILE_NAME = "notes.json"

    def __init__(self):
        self.notes = self.load_notes()

    def load_notes(self):
        try:
            with open(self.FILE_NAME, 'r', encoding='utf-8') as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def save_notes(self):
        with open(self.FILE_NAME, 'w', encoding='utf-8') as file:
            json.dump(self.notes, file, ensure_ascii=False, indent=4)

    def create_note(self):
        title = input("Введите заголовок заметки: ")
        content = input("Введите содержимое заметки: ")
        timestamp = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        note = {
            "id": len(self.notes) + 1,
            "title": title,
            "content": content,
            "timestamp": timestamp
        }
        self.notes.append(note)
        self.save_notes()
        print("Заметка создана.")

    def view_notes(self):
        if not self.notes:
            print("Список заметок пуст.")
            return
        for note in self.notes:
            print(f"[{note['id']}] {note['title']} ({note['timestamp']})")

    def view_note_details(self):
        self.view_notes()
        try:
            note_id = int(input("Введите ID заметки: "))
            note = next((n for n in self.notes if n["id"] == note_id), None)
            if note:
                print(f"Заголовок: {note['title']}\nСодержимое: {note['content']}\nДата: {note['timestamp']}")
            else:
                print("Заметка не найдена.")
        except ValueError:
            print("Неверный ввод.")

    def edit_note(self):
        self.view_notes()
        try:
            note_id = int(input("Введите ID заметки для редактирования: "))
            note = next((n for n in self.notes if n["id"] == note_id), None)
            if note:
                note['title'] = input("Введите новый заголовок: ") or note['title']
                note['content'] = input("Введите новое содержимое: ") or note['content']
                note['timestamp'] = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
                self.save_notes()
                print("Заметка обновлена.")
            else:
                print("Заметка не найдена.")
        except ValueError:
            print("Неверный ввод.")

    def delete_note(self):
        self.view_notes()
        try:
            note_id = int(input("Введите ID заметки для удаления: "))
            self.notes = [n for n in self.notes if n["id"] != note_id]
            self.save_notes()
            print("Заметка удалена.")
        except ValueError:
            print("Неверный ввод.")

    def export_to_csv(self):
        filename = input("Введите имя файла для экспорта (например, notes.csv): ")
        with open(filename, 'w', encoding='utf-8', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=["id", "title", "content", "timestamp"])
            writer.writeheader()
            writer.writerows(self.notes)
        print(f"Заметки экспортированы в файл {filename}.")

    def import_from_csv(self):
        filename = input("Введите имя файла для импорта (например, notes.csv): ")
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    row["id"] = int(row["id"])
                    self.notes.append(row)
                self.save_notes()
            print(f"Заметки импортированы из файла {filename}.")
        except FileNotFoundError:
            print("Файл не найден.")

    def menu(self):
        while True:
            print("\nУправление заметками:")
            print("1. Создать заметку")
            print("2. Просмотреть список заметок")
            print("3. Просмотреть подробности заметки")
            print("4. Редактировать заметку")
            print("5. Удалить заметку")
            print("6. Экспортировать в CSV")
            print("7. Импортировать из CSV")
            print("8. Вернуться в главное меню")

            choice = input("Выберите действие: ")
            if choice == "1":
                self.create_note()
            elif choice == "2":
                self.view_notes()
            elif choice == "3":
                self.view_note_details()
            elif choice == "4":
                self.edit_note()
            elif choice == "5":
                self.delete_note()
            elif choice == "6":
                self.export_to_csv()
            elif choice == "7":
                self.import_from_csv()
            elif choice == "8":
                break
            else:
                print("Неверный ввод. Попробуйте снова.")