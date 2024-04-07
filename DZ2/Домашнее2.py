from csv import DictWriter, DictReader
import os

def get_info():
    name = input("Введите имя: ")
    last_name = input("Введите фамилию: ")
    phone = input("Введите номер телефона: ")
    return name, last_name, phone

def append_file(file_name, info):
    with open(file_name, 'a', encoding='utf-8', newline='') as data:
        f_writer = DictWriter(data, fieldnames=['Имя', 'Фамилия', 'Телефон'])
        if os.stat(file_name).st_size == 0:
            f_writer.writeheader()
        f_writer.writerow({'Имя': info[0], 'Фамилия': info[1], 'Телефон': info[2]})

def read_file(file_name):
    with open(file_name, 'r', encoding='utf-8', newline='') as data:
        f_reader = DictReader(data)
        res = []
        for row in f_reader:
            res.append(row)
        return res

def update_file(file_name, key, value):
    res = read_file(file_name)
    updated = False
    for row in res:
        if row["Имя"] == value or row["Фамилия"] == value:
            new_info = get_info()
            row["Имя"] = new_info[0]
            row["Фамилия"] = new_info[1]
            row["Телефон"] = new_info[2]
            updated = True
            break
    if not updated:
        print("Запись с таким именем или фамилией не найдена")
    else:
        with open(file_name, "w", encoding='utf-8', newline='') as data:
            f_writer = DictWriter(data, fieldnames=['Имя', 'Фамилия', 'Телефон'])
            f_writer.writeheader()
            f_writer.writerows(res)

def delete_file(file_name, key, value):
    res = read_file(file_name)
    deleted = False
    for row in res:
        if row["Имя"] == value or row["Фамилия"] == value:
            res.remove(row)
            deleted = True
            break
    if not deleted:
        print("Запись с таким именем или фамилией не найдена")
    else:
        with open(file_name, "w", encoding='utf-8', newline='') as data:
            f_writer = DictWriter(data, fieldnames=['Имя', 'Фамилия', 'Телефон'])
            f_writer.writeheader()
            f_writer.writerows(res)

file_name = 'contacts.csv'

while True:
    command = input("Выберите действие: (a - добавить, u - обновить, d - удалить, v - просмотр, q - выход): ")

    if command == 'a':
        new_info = get_info()
        append_file(file_name, new_info)
    elif command == 'u':
        if not os.path.exists(file_name):
            print("Файл отсутствует. Создайте его")
            continue
        key = input("Введите ключ (имя/фамилия), по которому нужно обновить данные: ")
        value = input("Введите значение ключа: ")
        update_file(file_name, key, value)
    elif command == 'd':
        if not os.path.exists(file_name):
            print("Файл отсутствует. Создайте его")
            continue
        key = input("Введите ключ (имя/фамилия), по которому нужно удалить данные: ")
        value = input("Введите значение ключа: ")
        delete_file(file_name, key, value)
    elif command == 'v':
        if not os.path.exists(file_name):
            print("Файл отсутствует. Создайте его")
        else:
            for contact in read_file(file_name):
                print(contact)
    elif command == 'q':
        print("Программа завершена")
        break