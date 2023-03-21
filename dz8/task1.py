def show_menu() -> int:
    print("\nВыберите необходимое действие:\n"
          "1. Отобразить весь справочник\n"
          "2. Найти абонента по фамилии\n"
          "3. Найти абонента по номеру телефона\n"
          "4. Добавить абонента в справочник\n"
          "5. Сохранить справочник в текстовом формате\n"
          "6. Завершить работу\n")
    choice = int(input())
    return choice


def read(filename):
    data = []
    data1 = ('Фамилия','Имя','Телефон','Описание')
    with open(filename, 'r', encoding='utf-8') as fin:
        for line in fin:
            record = dict(zip(data1, line.strip().split(',')))
            data.append(record)
    print(data)
read('phon.txt')

        