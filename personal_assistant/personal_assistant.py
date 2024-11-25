from notes import NotesManager
from tasks import TasksManager
from contacts import ContactsManager
from finance import FinanceManager
from calculator import Calculator


def main_menu():
    while True:
        print("\nДобро пожаловать в Персональный помощник!")
        print("Выберите действие:")
        print("1. Управление заметками")
        print("2. Управление задачами")
        print("3. Управление контактами")
        print("4. Управление финансовыми записями")
        print("5. Калькулятор")
        print("6. Выход")

        choice = input("Введите номер действия: ")

        if choice == "1":
            NotesManager().menu()
        elif choice == "2":
            TasksManager().menu()
        elif choice == "3":
            ContactsManager().menu()
        elif choice == "4":
            FinanceManager().menu()
        elif choice == "5":
            Calculator().menu()
        elif choice == "6":
            print("До свидания!")
            break
        else:
            print("Неверный ввод. Попробуйте снова.")


if __name__ == "__main__":
    main_menu()