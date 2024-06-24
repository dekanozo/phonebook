class PhoneBook:
    def __init__(self, load_from_file=None):
        self.contacts = {}
        if load_from_file:
            self.load_contacts_from_file(load_from_file)

    def add_contact(self, identifier, first_name, last_name, phone):
        # Your existing code for adding contacts

    def delete_contact(self, identifier):
        # Your existing code for deleting contacts

    def update_contact(self, identifier, first_name=None, last_name=None, phone=None):
        # Your existing code for updating contacts

    def search_contact(self, query):
        # Your existing code for searching contacts

    def delete_contact_by_name(self, query):
        # Your existing code for deleting contacts by name

    def update_contact_by_name(self, query, first_name=None, last_name=None, phone=None):
        # Your existing code for updating contacts by name

    def display_contacts(self):
        # Your existing code for displaying contacts

    def save_contacts_to_file(self, filename):
        with open(filename, 'w', encoding='utf-8') as file:
            for identifier, info in self.contacts.items():
                file.write(f"{identifier},{info['first_name']},{info['last_name']},{info['phone']}\n")

    def load_contacts_from_file(self, filename):
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                parts = line.strip().split(',')
                identifier = parts[0]
                first_name = parts[1]
                last_name = parts[2]
                phone = parts[3]
                self.contacts[identifier] = {
                    'first_name': first_name,
                    'last_name': last_name,
                    'phone': phone
                }

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
8. сохранить - Сохранить текущие контакты в файл contacts.txt
9. загрузить - Загрузить контакты из файла contacts.txt
10. выход - Выйти из телефонного справочника
"""

    while True:
        print(commands)
        command = input("Введите команду: ").strip().lower()

        if command == "добавить":
            # Your existing command handling code

        elif command == "обновить":
            # Your existing command handling code

        elif command == "удалить":
            # Your existing command handling code

        elif command == "искать":
            # Your existing command handling code

        elif command == "удалить_по_имени":
            # Your existing command handling code

        elif command == "обновить_по_имени":
            # Your existing command handling code

        elif command == "показать":
            # Your existing command handling code

        elif command == "сохранить":
            phonebook.save_contacts_to_file('contacts.txt')
            print("Контакты сохранены в файл contacts.txt.")

        elif command == "загрузить":
            phonebook.load_contacts_from_file('contacts.txt')
            print("Контакты загружены из файла contacts.txt.")

        elif command == "выход":
            print("Выход из телефонного справочника.")
            break

        else:
            print("Неверная команда. Попробуйте еще раз.")

if __name__ == "__main__":
    main()