import json
import csv

class FinanceManager:
    FILE_NAME = "finance.json"

    def __init__(self):
        self.records = self.load_records()

    def load_records(self):
        try:
            with open(self.FILE_NAME, 'r', encoding='utf-8') as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def save_records(self):
        with open(self.FILE_NAME, 'w', encoding='utf-8') as file:
            json.dump(self.records, file)

    def add_record(self):
        amount = float(input("Введите сумму (отрицательная для расходов, положительная для доходов): "))
        category = input("Введите категорию (например, Еда, Транспорт): ")
        date = input("Введите дату операции (ДД-ММ-ГГГГ): ")
        description = input("Введите описание операции: ")
        record = {
            "id": len(self.records) + 1,
            "amount": amount,
            "category": category,
            "date": date,
            "description": description
        }
        self.records.append(record)
        self.save_records()
        print("Запись добавлена.")

    def view_records(self):
        if not self.records:
            print("Список записей пуст.")
            return
        for record in self.records:
            print(f"[{record['id']}] {record['category']} | {record['amount']} | Дата: {record['date']} | Описание: {record['description']}")

    def filter_records(self):
        category = input("Введите категорию для фильтрации: ")
        filtered = [r for r in self.records if r["category"].lower() == category.lower()]
        if filtered:
            for record in filtered:
                print(f"[{record['id']}] {record['category']} | {record['amount']} | Дата: {record['date']} | Описание: {record['description']}")
        else:
            print("Записей не найдено.")

    def calculate_balance(self):
        total = sum(r["amount"] for r in self.records)
        print(f"Общий баланс: {total}")

    def export_to_csv(self):
        filename = input("Введите имя файла для экспорта (например, finance.csv): ")
        with open(filename, 'w', encoding='utf-8', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=["id", "amount", "category", "date", "description"])
            writer.writeheader()
            writer.writerows(self.records)
        print(f"Финансовые записи экспортированы в файл {filename}.")

    def import_from_csv(self):
        filename = input("Введите имя файла для импорта (например, finance.csv): ")
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    row["id"] = int(row["id"])
                    row["amount"] = float(row["amount"])
                    self.records.append(row)
                self.save_records()
            print(f"Финансовые записи импортированы из файла {filename}.")
        except FileNotFoundError:
            print("Файл не найден.")

    def menu(self):
        while True:
            print("\nУправление финансовыми записями:")
            print("1. Добавить запись")
            print("2. Просмотреть записи")
            print("3. Фильтровать записи")
            print("4. Подсчитать общий баланс")
            print("5. Экспортировать в CSV")
            print("6. Импортировать из CSV")
            print("7. Вернуться в главное меню")

            choice = input("Выберите действие: ")
            if choice == "1":
                self.add_record()
            elif choice == "2":
                self.view_records()
            elif choice == "3":
                self.filter_records()
            elif choice == "4":
                self.calculate_balance()
            elif choice == "5":
                self.export_to_csv()
            elif choice == "6":
                self.import_from_csv()
            elif choice == "7":
                break
            else:
                print("Неверный ввод. Попробуйте снова.")
