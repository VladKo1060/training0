class Human:
    '''
    Класс человека
    Форматы аргументов:
    name - Строка - Имя
    middle_name - Строка - Отчество
    surname - Строка - Фамилия
    phone_number - Срока - Телефон в формате +7 123 456 78 90
    birthday - Строка - дата в формате ДД.ММ.ГГГГ
    '''

    def __init__(
            self,
            name: str = 'No name',
            middle_name: str = 'No middle_name',
            surname: str = 'No surname',
            phone_number: str = 'No phone_number',
            birthday: str = 'No birthday'
    ):
        self.name: str = name
        self.middle_name: str = middle_name
        self.surname: str = surname
        self.phone_number: str = phone_number
        self.birthday: str = birthday

    def data_print(self):
        print(f'Имя {self.name}')
        print(f'Отчество {self.middle_name}')
        print(f'Фамилия {self.surname}')
        print(f'Телефонный номер {self.phone_number}')
        print(f'День рождения {self.birthday}')

    def data_dictionary(self):
        return {
            'name': self.name,
            'middle_name': self.middle_name,
            'surname': self.surname,
            'phone_number': self.phone_number,
            'birthday': self.birthday
        }


if __name__ == '__main__':
    human = Human('Имя', 'Отчество', 'Фамилия', '+7 123 456 78 90', 'ДД.ММ.ГГГГ')
    human.data_print()
    print(human.data_dictionary())
