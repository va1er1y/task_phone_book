import re
import csv

def read_file():
    with open("phonebook_raw.csv", encoding="utf-8") as f:
        rows = csv.reader(f, delimiter=",")
        return list(rows)

# получаем фио разбитые как перечисление через запятую
def treatment_data():
    prelimary_contact_list = {}
    num = 1
    union_name = []
    contacts_list = read_file()
    for position in contacts_list:
        prelimary_contact_list[num] = (" ".join(position[0:3:1])).split()
        if 0 < len(prelimary_contact_list[num]) <= 2:
            prelimary_contact_list[num].extend(' ')
        prelimary_contact_list[num].extend(position[3:7:])
        num = 1 + num
    data = list(prelimary_contact_list.values())
    for i in range(len(data)):
        name = data.pop()
        for value in data:
            if str(name[0:2:]) in str(value[0:2:]):
                for numer in range(len(name)):
                    if not name[numer] == value[numer]:
                        name[numer] = (" ".join([name[numer], value[numer]]))
                union_name.append(name)
    data = list(prelimary_contact_list.values())
    datas = list(prelimary_contact_list.values())
    for u_name in union_name:
        for i in range(len(data)):
            a = data[i]
            if str(u_name[0:2:]) in str(a[0:2:]):
                datas.remove(a)
    for u_name in union_name:
        datas.append(u_name)

    pattern = re.compile(r"(\+7|8)\s?\(?(\d{3})\)?[\s\-]?(\d{3})[-\s]?(\d{2})[-\s]?(\d{2})\s?\(?(доб.)?\s*(\d+)?\)?")
    for i in datas:
        i[5] = (pattern.sub(r"+7(\2)\3\4\5\6\7", i[5]))
    return datas

# код для записи файла в формате CSV
def write_phone_book():

    with open("phonebook.csv", "w") as f:
        datawriter = csv.writer(f, delimiter=',')
        datawriter.writerows(treatment_data())
if __name__ == '__main__':
    write_phone_book()