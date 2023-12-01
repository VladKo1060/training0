class Data_Base:
    """
    Класс работы с текстовыми файлами в качестве баз данных
    Класс написан под определённые задачи, поэтому у него такая неуневерсальная архитектура
    """

    def __init__(self, file_name: str = 'Data_Base'):
        self.file_name = file_name
        with open(self.file_name, 'a', encoding='UTF-8') as file:
            pass

    def write_to_date_base(self,                                                                                        # TODO ренайминг
                           date_base_id: int = None,
                           surname: str = None,
                           name: str = None,
                           middle_name: str = None,
                           phone_number: str = None,
                           birthday: str = None
                           ):
        with open(self.file_name, 'a', encoding='UTF-8') as file:
            file.write(f'{date_base_id}\t')
            file.write(f'{surname}\t')
            file.write(f'{name}\t')
            file.write(f'{middle_name}\t')
            file.write(f'{phone_number}\t')
            file.write(f'{birthday}\n')

    def scan_and_write_to_date_base(self,                                                                               # TODO ренайминг
                                    date_base_id: int = None,
                                    surname: str = None,
                                    name: str = None,
                                    middle_name: str = None,
                                    phone_number: str = None,
                                    birthday: str = None
                                    ):
        with open(self.file_name, 'r', encoding='UTF-8') as file:
            for s in file.readlines():
                if str(date_base_id) in s:
                    return False
        with open(self.file_name, 'a', encoding='UTF-8') as file:
            file.write(f'{date_base_id}\t')
            file.write(f'{surname}\t')
            file.write(f'{name}\t')
            file.write(f'{middle_name}\t')
            file.write(f'{phone_number}\t')
            file.write(f'{birthday}\n')
            return True

    def scan_and_delite_write_to_date_base(self,                                                                        # TODO ренайминг
                                           date_base_id: int,
                                           surname: str,
                                           name: str,
                                           middle_name: str,
                                           phone_number: str,
                                           birthday: str
                                           ):
        flag = False
        new_data = ''
        line_number = 0
        line_feed_number = 0
        end_line_feed_number = 0
        with open(self.file_name, 'r', encoding='UTF-8') as file:
            for s in file.readlines():
                if str(date_base_id) in s:
                    len_s = len(s)
                    break
                line_number += 1

        with open(self.file_name, 'r', encoding='UTF-8') as f:
            old_data = f.read()

        for i in range(len(old_data)):
            if old_data[i] == '\n':
                if line_feed_number == line_number - 1:
                    end_line_feed_number = i
                    flag = True
                line_feed_number += 1
                # print(line_feed_number)
            if flag:
                break
        # print(line_feed_number, end_line_feed_number)

        new_data += old_data[
                    :end_line_feed_number + 1] + f'{date_base_id}\t{surname}\t{name}\t{middle_name}\t{phone_number}\t{birthday}' + old_data[
                                                                                                                                   end_line_feed_number + len_s:]

        # new_data = old_data.replace('что_меняем', 'на_что_меняем')

        with open(self.file_name, 'w', encoding='UTF-8') as f:
            f.write(new_data)

        # f'{date_base_id}\t{surname}\t{name}\t{middle_name}\t{phone_number}\t{birthday}\n'

    def find_user_by_id(self, userid: int):                                                                             # TODO ренайминг
        with open(self.file_name, 'r', encoding='UTF-8') as file:
            for line in file.readlines():
                user_data = line.strip().split('\t')
                if str(userid) in user_data[0]:
                    return user_data # {'id': user_data[0],
                           #  'surname': user_data[1],
                           #  'name': user_data[3],
                           #  'middle_name': user_data[4],
                           #  'phone_number': user_data[5],
                           #  'birthday': user_data[6]
                           #  }


if __name__ == '__main__':
    db = Data_Base('Bot_Date_Base')
    # db.write_to_date_base(1, 'uipwregb', 'oirtgbjn', 'oeritgbjnk', 'iojhrb', 'eoibjke')
    print(db.find_user_by_id(1752005502))
