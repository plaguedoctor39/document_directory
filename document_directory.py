documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]
directories = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006', '5400 028765', '5455 002299'],
    '3': []
}


def find_document_owner(doc_num):
    for document in documents:
        if document['number'] == str(doc_num):
            return document["name"]
    print(f'Документа с номером {doc_num} нету в базе')
    return 0


def document_number_info(doc_num):
    for document in documents:
        if document['number'] == str(doc_num):
            return f'{document["type"]} \"{document["number"]}\" \"{document["name"]}\"'
    print(f'Документа с номером {doc_num} нету в базе')
    return 0


def find_shelf(doc_num):
    for directory in directories:
        if str(doc_num) in directories[directory]:
            return directory
    print(f'Документа с номером {doc_num} нету ни в одной директории')
    return 0


def add_document(docs, dirs):
    doc_num = input('Введите номер документа - ')
    doc_type = input('Введите тип документа - ')
    doc_owner = input('Введите владельца документа - ')
    try:
        if doc_owner == '':
            raise KeyError
    except KeyError:
        print('Не введено поле name у документа')
        return 0
    doc_directory = input('Введите номер директории, в которой будет храниться документ - ')
    if doc_directory  in dirs:
        if str(doc_num) not in dirs[str(doc_directory)]:
            dirs[doc_directory].append(doc_num)
            new_doc = {
                "type": doc_type,
                "number": doc_num,
                "name": doc_owner
            }
            docs.append(new_doc)
            print(documents)
            return docs, dirs
        else:
            print(f'Документ {doc_num} уже есть в данной директории')
            return 0
    else:
        print(f'Директории с номером {doc_directory} не существует')
        return 0


def delete_document(doc_num):
    for document in documents:
        if str(doc_num) == document['number']:
            documents.remove(document)
            directories[find_shelf(doc_num)].remove(doc_num)
            print(f'Документ {doc_num} был удален из каталога')
            print(documents)
            print(directories)
            return 0
        else:
            pass
    print(f'Документа {doc_num} нету ни в одном каталоге')
    return 0


def document_move(doc_num, target_shelf):
    actual_shelf = str(find_shelf(doc_num))
    if actual_shelf in directories:
        if target_shelf in directories:
            directories[target_shelf].append(doc_num)
            directories[actual_shelf].remove(doc_num)
            print(f'Документ {doc_num} был перемещен из директории {actual_shelf} в директорию {target_shelf}')
            print(directories)
        else:
            print('Такой директории не существует, желаете создать? ')
            if input() == 'да':
                add_shelf()
            else:
                return 0
    return 0


def add_shelf():
    new_shelf = input('Введите номер директории - ')
    if str(new_shelf) not in directories:
        directories[new_shelf] = []
        print(f'Директория с номером {new_shelf} была добавлена')
        print(directories)
    else:
        print(f'Директория с номером {new_shelf} уже существует')
        return 0


def show_all_names():
    for document in documents:
        print(document['name'])


def runner():
    while True:
        cmd = input('Введите команду - ')
        if cmd == 'p' or cmd == 'people':
            doc_num = input('Введите номер документа - ')
            if find_document_owner(doc_num) != 0:
                print(find_document_owner(doc_num))
        elif cmd == 'l' or cmd == 'list':
            doc_num = input('Введите номер документа - ')
            if document_number_info(doc_num) != 0:
                print(document_number_info(doc_num))
        elif cmd == 's' or cmd == 'shelf':
            doc_num = input('Введите номер документа - ')
            if find_shelf(doc_num) != 0:
                print(f'Документ с номером {doc_num} находится в директории под номером {find_shelf(doc_num)}')
        elif cmd == 'a' or cmd == 'add':
            add_document(documents, directories)
        elif cmd == 'd' or cmd == 'delete':
            doc_num = input('Введите номер документа - ')
            delete_document(doc_num)
        elif cmd == 'm' or cmd == 'move':
            doc_num = input('Введите номер документа - ')
            target_shelf = input('Введите номер директории - ')
            document_move(str(doc_num), str(target_shelf))
            print(documents)
        elif cmd == 'as' or cmd == 'add shelf':
            add_shelf()
        elif cmd == 'e' or cmd == 'end':
            print('Программа завершена')
            break
        elif cmd == 'an' or cmd == 'all names':
            show_all_names()
        else:
            print('Вы ввели неверную команду или её нету в списке доступных команд')

runner()