class Data_Base:

    def __init__(self, file_name: str = 'Data_Base'):
        self.file_name = file_name

    def write_to_date_base(self,
                           date_base_id: int,
                           surname: str,
                           name: str,
                           middle_name: str,
                           phone_number: str,
                           birthday: str
                           ):
        with open(self.file_name, 'a', encoding='UTF-8') as file:
            file.write(f'{date_base_id}\t')
            file.write(f'{surname}\t')
            file.write(f'{name}\t')
            file.write(f'{middle_name}\t')
            file.write(f'{phone_number}\t')
            file.write(f'{birthday}\n')




if __name__ == '__main__':
    db = Data_Base()
    db.write_to_date_base(1, 'surname', 'name', 'middle_name', 'phone_number', 'birthday')
