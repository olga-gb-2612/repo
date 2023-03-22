#!/usr/bin/python3
# coding: utf-8


class PhoneBook:

    def __init__(self, phone_book_filename):
        self.phone_book = []
        self.phone_book_filename = phone_book_filename

        self.keys = ('Фамилия', 'Имя', 'Телефон', 'Описание')

        self.read_phone_book_from_file()

    def __str__(self):
        return f'{self.phone_book}'

    def read_phone_book_from_file(self):

        phone_book = []
        with open(self.phone_book_filename, 'r', encoding='utf-8') as fin:
            for line in fin:
                record = dict(zip(self.keys, line.strip().split(',')))
                phone_book.append(record)
        self.phone_book = phone_book
        print(f'Телефонный справочник прочитан из файла {self.phone_book_filename}')

    def write_phone_book_to_file(self):
        with open(self.phone_book_filename, 'w', encoding='utf-8') as fout:
            for record in self.phone_book:
                fout.write(f'{record["Фамилия"]},{record["Имя"]},{record["Телефон"]},{record["Описание"]}\n')
        print(f'Телефонный справочник записан в файл {self.phone_book_filename}')

    def print_phone_book(self):
        for record in self.phone_book:
            print(record)

    def find_records_with_substr(self, what_find):

        found_index_records = []  # Индексы найденных записей

        for index in range(len(self.phone_book)):
            record = self.phone_book[index]
            if record["Фамилия"].lower().find(what_find) >= 0 \
                    or record["Имя"].lower().find(what_find) >= 0 \
                    or record["Телефон"].lower().find(what_find) >= 0 \
                    or record["Описание"].lower().find(what_find) >= 0:
                found_index_records.append(index)

        return found_index_records

    def find_and_print_records_with_sustr(self):

        what_find = input('Введите полностью или часть любого поля: ')
        found_index_records = self.find_records_with_substr(what_find)
        print(found_index_records)

        if len(found_index_records) > 0:
            # Что-то нашли, выводим эти записи
            print(f'Найдено записей: {len(found_index_records)}')
            for index in found_index_records:
                record = self.phone_book[index]
                print(record)
        else:
            print(f'По вашему запросу "{what_find}" ничего не найдено')

    def add_record(self):

        last_name = input('Введите фамилию: ')
        first_name = input('Введите имя: ')
        phone = input('Введите телефон: ')
        description = input('Введите описание: ')

        record = dict(zip(self.keys, [last_name, first_name, phone, description]))
        self.phone_book.append(record)
        self.write_phone_book_to_file()

    def delete_record(self):

        what_find = input('Введите полностью или часть записи, которую хотите удалить: ')
        found_index_records = self.find_records_with_substr(what_find)
        print(found_index_records)

        if len(found_index_records) > 0:
            # Что-то нашли, выводим эти записи
            print(f'Найдено записей: {len(found_index_records)}')
            for index in found_index_records:
                record = self.phone_book[index]
                print(record)
            what_index = int(input('Введите номер индекса удаляемой записи: '))
            print(f'Удалена запись: {self.phone_book.pop(what_index)}')
            self.write_phone_book_to_file()
        else:
            print(f'По вашему запросу "{what_find}" ничего не найдено')

    @staticmethod
    def show_menu():
        print("\nВыберите необходимое действие:\n"
              "1. Отобразить весь справочник\n"
              "2. Найти абонента\n"
              "3. Добавить абонента в справочник\n"
              "4. Сохранить справочник в текстовом формате\n"
              "5. Удалить запись\n")
        return int(input())

    def loop(self):

        while True:

            choice = self.show_menu()
            if choice == 1:
                self.print_phone_book()

            elif choice == 2:
                self.find_and_print_records_with_sustr()

            elif choice == 3:
                self.add_record()

            elif choice == 4:
                self.write_phone_book_to_file()

            elif choice == 5:
                self.delete_record()
                #break

            else:
                print("Выбрано неверное действие, повторите заново >:-|")


if __name__ == '__main__':

    pb = PhoneBook('phon.txt')
    pb.loop()
