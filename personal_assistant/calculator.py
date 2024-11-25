class Calculator:
    def evaluate_expression(self):
        try:
            expression = input("Введите математическое выражение (например, 2 + 2 * 3): ")
            result = eval(expression, {"__builtins__": None}, {})
            print(f"Результат: {result}")
        except ZeroDivisionError:
            print("Ошибка: деление на ноль!")
        except Exception as e:
            print(f"Ошибка: {e}")

    def menu(self):
        while True:
            print("\nКалькулятор:")
            print("1. Вычислить выражение")
            print("2. Вернуться в главное меню")

            choice = input("Выберите действие: ")
            if choice == "1":
                self.evaluate_expression()
            elif choice == "2":
                break
            else:
                print("Неверный ввод. Попробуйте снова.")
