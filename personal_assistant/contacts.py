import json
import csv

class ContactsManager:
    FILE_NAME = "contacts.json"

    def __init__(self):
        self.contacts = self.load_contacts()

    def load_contacts(self):
        try:
            with open(self.FILE_NAME, 'r', encoding='utf-8') as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def save_contacts(self):
        with open(self.FILE_NAME, 'w', encoding='utf-8') as file:
            json.dump(self.contacts, file, ensure_ascii=False, indent=4)

    def add_contact(self):
        name = input("Введите имя контакта: ")
        phone = input("Введите номер телефона: ")
        email = input("Введите адрес электронной почты: ")
        contact = {
            "id": len(self.contacts) + 1,
            "name": name,
            "phone": phone,
            "email": email
        }
        self.contacts.append(contact)
        self.save_contacts()
        print("Контакт добавлен.")

    def view_contacts(self):
        if not self.contacts:
            print("Список контактов пуст.")
            return
        for contact in self.contacts:
            print(f"[{contact['id']}] {contact['name']} | Телефон: {contact['phone']} | Email: {contact['email']}")

    def search_contact(self):
        query = input("Введите имя или номер телефона для поиска: ").lower()
        results = [c for c in self.contacts if query in c["name"].lower() or query in c["phone"]]
        if results:
            for contact in results:
                print(f"[{contact['id']}] {contact['name']} | Телефон: {contact['phone']} | Email: {contact['email']}")
        else:
            print("Контакты не найдены.")

    def edit_contact(self):
        self.view_contacts()
        try:
            contact_id = int(input("Введите ID контакта для редактирования: "))
            contact = next((c for c in self.contacts if c["id"] == contact_id), None)
            if contact:
                contact["name"] = input("Введите новое имя: ") or contact["name"]
                contact["phone"] = input("Введите новый телефон: ") or contact["phone"]
                contact["email"] = input("Введите новый email: ") or contact["email"]
                self.save_contacts()
                print("Контакт обновлен.")
            else:
                print("Контакт не найден.")
        except ValueError:
            print("Неверный ввод.")

    def delete_contact(self):
        self.view_contacts()
        try:
            contact_id = int(input("Введите ID контакта для удаления: "))
            self.contacts = [c for c in self.contacts if c["id"] != contact_id]
            self.save_contacts()
            print("Контакт удален.")
        except ValueError:
            print("Неверный ввод.")

    def export_to_csv(self):
        filename = input("Введите имя файла для экспорта (например, contacts.csv): ")
        with open(filename, 'w', encoding='utf-8', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=["id", "name", "phone", "email"])
            writer.writeheader()
            writer.writerows(self.contacts)
        print(f"Контакты экспортированы в файл {filename}.")

    def import_from_csv(self):
        filename = input("Введите имя файла для импорта (например, contacts.csv): ")
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    row["id"] = int(row["id"])
                    self.contacts.append(row)
                self.save_contacts()
            print(f"Контакты импортированы из файла {filename}.")
        except FileNotFoundError:
            print("Файл не найден.")

    def menu(self):
        while True:
            print("\nУправление контактами:")
            print("1. Добавить контакт")
            print("2. Просмотреть список контактов")
            print("3. Найти контакт")
            print("4. Редактировать контакт")
            print("5. Удалить контакт")
            print("6. Экспортировать в CSV")
            print("7. Импортировать из CSV")
            print("8. Вернуться в главное меню")

            choice = input("Выберите действие: ")
            if choice == "1":
                self.add_contact()
            elif choice == "2":
                self.view_contacts()
            elif choice == "3":
                self.search_contact()
            elif choice == "4":
                self.edit_contact()
            elif choice == "5":
                self.delete_contact()
            elif choice == "6":
                self.export_to_csv()
            elif choice == "7":
                self.import_from_csv()
            elif choice == "8":
                break
            else:
                print("Неверный ввод. Попробуйте снова.")
