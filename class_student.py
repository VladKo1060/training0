from statistics import mean
from random import choice

class Student:
    """
    Класс описания учиника

    аргументы:
     name - имя учиника
     age - возраст учиника
     grade - класс учиника
     favorite_subject - любимый предмет учиника
     performance - оценки
     classroom_teacher - классный руководитель
     personality_type - тип мышления(технарь, гуманитарий, химбио)
    """
    def __init__(self, name: str = "Вася", age: int = 7, grade: str = "1А", favorite_subject: str = None,
                 performance: dict = [5], classroom_teacher: str = "Дмитрий Валерьевич Акимов",
                 personality_type: str = "технарь"):
        self.name = name
        self.age = age
        self.grade = grade
        self.favorite_subject = favorite_subject
        self.performance = performance
        self.classroom_teacher = classroom_teacher
        self.personality_type = personality_type


    def says_hello_teacher(self):
        print(f'Здравствуйте {self.classroom_teacher}! Я {self.name}, мне {self.age} лет.')


    def hit(self, enemy):
        if self.grade == enemy.grade:
            print(f'Махач отменяется!!! Мы, {self.name} и {enemy.name}, однакласники!!!')
            return None
        if self.favorite_subject == enemy.favorite_subject:
            print(f'Махач отменяется!!! Мы, {self.name} и {enemy.name}, любим один предмет!!!')
            return None
        if self.personality_type == enemy.personality_type:
            print(f'Махач отменяется!!! Мы, {self.name} и {enemy.name}, мыслим одинаково!!!')
            return None
        if round(float(mean(enemy.performance)), 1) >= 4.6 and round(float(mean(self.performance)), 1) >= 4.6:
            print(f'Махач отменяется!!! Мы отличники, мы учимся')
            return None
        if round(float(mean(self.performance)), 1) >= 4.6:
            print(f'Махач отменяется!!! Я не умею бить лицо...')
            return None
        if round(float(mean(enemy.performance)), 1) >= 4.6:
            print(f'Махач отменяется!!! Я отличников не бью')
            return None
        print(f'Победитель махача {choice([self.name, enemy.name])}')


class Normal_Student(Student):
    '''
    Подклассс класса студент
    '''
    def __init__(self, name: str = "Вася", age: int = 7, grade: str = "1А", favorite_subject: str = None,
                 performance: dict = [4], classroom_teacher: str = "Дмитрий Валерьевич Акимов",
                 personality_type: str = "технарь"):
        super().__init__(name, age, grade, favorite_subject, performance, classroom_teacher, personality_type)

    def scip_lesson(self):
        if round(float(mean(self.performance)), 1) <= 3.6:
            print(f'Я прогулял урок! :(')
            self.performance += [2]
            return None
        elif 3.6 <= round(float(mean(self.performance)), 1) <= 4.6:
            print(f'Я не прогулял урок!')
            self.performance += [choice([3, 4, 5])]
            return None
        elif 4.6 <= round(float(mean(self.performance)), 1):
            print(f'Я и не думал прогуливать урок!')
            self.performance += [choice([4, 5])]
            return None


class Social_Activity(Normal_Student):
    '''
    Подклассс класса нормальный студент
    '''

    def __init__(self, name: str = "Вася", age: int = 7, grade: str = "1А", favorite_subject: str = None,
                 performance: dict = [4], classroom_teacher: str = "Дмитрий Валерьевич Акимов",
                 personality_type: str = "технарь", list_of_social_activities: dict = ['звукарь', 'участник совета школы']):
        super().__init__(name, age, grade, favorite_subject, performance, classroom_teacher, personality_type)
        self.social_activities = list_of_social_activities

    def go_to_party(self):
        if len(self.social_activities) >= 2:
            print(f'Совсем время нет!')
            return None
        print(f'Пошли!')


class Olympiadnik(Social_Activity):
    '''
    Подклассс класса социално активного студент
    '''

    def __init__(self, name: str = "Вася", age: int = 7, grade: str = "1А", favorite_subject: str = None,
                 performance: dict = [4], classroom_teacher: str = "Дмитрий Валерьевич Акимов",
                 personality_type: str = "технарь", list_of_social_activities: dict = [], list_of_olympic: dict = ['матиматика']):
        super().__init__(name, age, grade, favorite_subject, performance, classroom_teacher, personality_type, list_of_social_activities + ['олимпиады'])
        self.list_of_olympic = list_of_olympic

    def write_olimpiada(self, olympiad_number: int = 0):
        scores = [i for i in range(0, 101)]
        print(f'{self.name} получил на олимпиаде по предмету {self.list_of_olympic[olympiad_number]} {choice(scores)} баллов')

