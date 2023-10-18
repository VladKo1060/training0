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
