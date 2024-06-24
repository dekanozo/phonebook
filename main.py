class PhoneBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, identifier, first_name, last_name, phone):
        if identifier in self.contacts:
            print("Контакт с таким идентификатором уже существует.")
        else:
            self.contacts[identifier] = {
                'first_name': first_name,
                'last_name': last_name,
                'phone': phone
            }
            print(f"Контакт {first_name} {last_name} добавлен.")

    def delete_contact(self, identifier):
        if identifier in self.contacts:
            del self.contacts[identifier]
            print(f"Контакт с идентификатором {identifier} удален.")
        else:
            print("Контакт не найден.")

    def update_contact(self, identifier, first_name=None, last_name=None, phone=None):
        if identifier in self.contacts:
            if first_name:
                self.contacts[identifier]['first_name'] = first_name
            if last_name:
                self.contacts[identifier]['last_name'] = last_name
            if phone:
                self.contacts[identifier]['phone'] = phone
            print(f"Контакт с идентификатором {identifier} обновлен.")
        else:
            print("Контакт не найден.")

    def search_contact(self, query):
        results = []
        for identifier, info in self.contacts.items():
            if query.lower() in info['first_name'].lower() or query.lower() in info['last_name'].lower():
                results.append((identifier, info))
        return results

    def delete_contact_by_name(self, query):
        results = self.search_contact(query)
        for identifier, _ in results:
            del self.contacts[identifier]
        print(f"Контакты, соответствующие '{query}', удалены.")

    def update_contact_by_name(self, query, first_name=None, last_name=None, phone=None):
        results = self.search_contact(query)
        for identifier, _ in results:
            self.update_contact(identifier, first_name, last_name, phone)
        print(f"Контакты, соответствующие '{query}', обновлены.")

    def display_contacts(self):
        if self.contacts:
            for identifier, info in self.contacts.items():
                print(f"ID: {identifier}, Имя: {info['first_name']}, Фамилия: {info['last_name']}, Телефон: {info['phone']}")
        else:
            print("Контакты не найдены.")

def main():
    phonebook = PhoneBook()

    commands = """
Доступные команды:
1. добавить - Добавить новый контакт
2. обновить - Обновить существующий контакт
3. удалить - Удалить контакт по идентификатору
4. искать - Искать контакты по имени или фамилии
5. удалить_по_имени - Удалить контакты по имени или фамилии
6. обновить_по_имени - Обновить контакты по имени или фамилии
7. показать - Показать все контакты
8. выход - Выйти из телефонного справочника
"""

    while True:
        print(commands)
        command = input("Введите команду: ").strip().lower()

        if command == "добавить":
            identifier = input("Введите идентификатор: ")
            first_name = input("Введите имя: ")
            last_name = input("Введите фамилию: ")
            phone = input("Введите номер телефона: ")
            phonebook.add_contact(identifier, first_name, last_name, phone)

        elif command == "обновить":
            identifier = input("Введите идентификатор: ")
            first_name = input("Введите имя (или нажмите Enter, чтобы пропустить): ")
            last_name = input("Введите фамилию (или нажмите Enter, чтобы пропустить): ")
            phone = input("Введите номер телефона (или нажмите Enter, чтобы пропустить): ")
            phonebook.update_contact(identifier, first_name or None, last_name or None, phone or None)

        elif command == "удалить":
            identifier = input("Введите идентификатор: ")
            phonebook.delete_contact(identifier)

        elif command == "искать":
            query = input("Введите имя или фамилию для поиска: ")
            results = phonebook.search_contact(query)
            print("Результаты поиска:")
            for identifier, info in results:
                print(f"ID: {identifier}, Имя: {info['first_name']}, Фамилия: {info['last_name']}, Телефон: {info['phone']}")

        elif command == "удалить_по_имени":
            query = input("Введите имя или фамилию для удаления: ")
            phonebook.delete_contact_by_name(query)

        elif command == "обновить_по_имени":
            query = input("Введите имя или фамилию для обновления: ")
            first_name = input("Введите имя (или нажмите Enter, чтобы пропустить): ")
            last_name = input("Введите фамилию (или нажмите Enter, чтобы пропустить): ")
            phone = input("Введите номер телефона (или нажмите Enter, чтобы пропустить): ")
            phonebook.update_contact_by_name(query, first_name or None, last_name or None, phone or None)

        elif command == "показать":
            phonebook.display_contacts()

        elif command == "выход":
            print("Выход из телефонного справочника.")
            break

        else:
            print("Неверная команда. Попробуйте еще раз.")

if __name__ == "__main__":
    main()
