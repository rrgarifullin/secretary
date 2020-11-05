from data import documents, directories


def input_command():
    """
    Список доступных команд:
  p - команда, которая спросит номер документа и выведет имя человека, которому он принадлежит
  s - команда, которая спросит номер документа и выведет номер полки, на которой он находится
  l - команда, которая выведет список всех документов
  a - команда, которая добавит новый документ в каталог и в перечень полок, спросив его номер, тип, имя владельца и номер полки, на котором он будет храниться
  d - команда, которая спросит номер документа и удалит его из каталога и из перечня полок
  m - команда, которая спросит номер документа и целевую полку и переместит его с текущей полки на целевую
  as - команда, которая спросит номер новой полки и добавит ее в перечень
    """
    print('Чтобы посмотреть список команд введите h')
    while True:
        command = input('\nВведите команду: ')
        if command == 'p':
            doc_number = user_input('name')
            print(display_name(doc_number))
        elif command == 's':
            doc_number = user_input('shelves')
            print(display_shelf(doc_number))
        elif command == 'l':
            print(*display_list(), sep='\n')
        elif command == 'a':
            doc_number, doc_type, owner_name, shelf = user_input('add_doc')
            print(add_document(doc_number, doc_type, owner_name, shelf))
        elif command == 'd':
            doc_number = user_input('delete')
            print(delete_document(doc_number))
        elif command == 'm':
            doc_number, new_shelf = user_input('move')
            print(move_document(doc_number, new_shelf))
        elif command == 'as':
            new_shelf = user_input('add_shelf')
            print(add_new_shelf(new_shelf))
        elif command == 'h':
            print(input_command.__doc__)
        elif command == 'q':
            break


def user_input(flag):
    if flag == 'name' or flag == 'delete' or flag == 'shelves':
        doc_number = input('Введите номер документа: ')
        return doc_number
    elif flag == 'add_doc':
        doc_number = input('Введите номер документа: ')
        doc_type = input('Введите тип документа: ')
        owner_name = input('Введите имя владельца: ')
        shelf = input('Введите номер полки: ')
        return doc_number, doc_type, owner_name, shelf
    elif flag == 'move':
        doc_number = input('Введите номер документа: ')
        new_shelf = input('Введите целевую полку: ')
        return doc_number, new_shelf
    elif flag == 'add_shelf':
        new_shelf = input('Введите номер полки: ')
        return new_shelf


def display_name(doc_number):
    for document in documents:
        if document['number'] == doc_number:
            return document['name']
    else:
        return f'Документа с номером {doc_number} не существует'


def display_shelf(doc_number):
    for shelf, doc in directories.items():
        if doc_number in doc:
            return shelf
    else:
        return f'Документа с номером {doc_number} не существует'


def display_list():
    document_list = []
    for document in documents:
        doc = document['type'] + ' \"' + document['number'] + '\" \"' + document['name'] + '\"'
        document_list.append(doc)
    return document_list


def add_document(doc_number, doc_type, owner_name, shelf):
    if shelf in directories:
        documents.append({"type": doc_type, "number": doc_number, "name": owner_name})
        directories[shelf].append(doc_number)
        return f'Документ номер {doc_number} добавлен на полку {shelf}'
    else:
        return f'Полки номер {shelf} не существует'


def delete_document(doc_number):
    for doc in documents:
        if doc_number == doc['number']:
            documents.remove(doc)
            for shelf, numbers in directories.items():
                if doc_number in numbers:
                    directories[shelf].remove(doc_number)
                    return f'Документ номер {doc_number} удален'
    else:
        return f'Документа с номером {doc_number} не существует'


def move_document(doc_number, new_shelf):
    for shelf in directories.keys():
        if doc_number in directories[shelf] and new_shelf in directories.keys():
            directories[shelf].remove(doc_number)
            directories[new_shelf].append(doc_number)
            return f'Документ номер {doc_number} перемещен на полку {new_shelf}'
    else:
        return 'Документа или полки с такими номерами не существует'


def add_new_shelf(new_shelf):
    if new_shelf in directories.keys():
        return f'Полка {new_shelf} уже есть'
    else:
        directories[new_shelf] = []
        return f'Полка {new_shelf} создана'


if __name__ == '__main__':
    input_command()