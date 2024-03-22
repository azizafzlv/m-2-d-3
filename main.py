#1
"""
Создать класс Book с атрибутами (свойство) title (название),
author (автор) и pages (кол-во страниц). Добавить метод
info, который возвращает инфу о книге в виде строки
"""

# class Book:
#     def __init__(self, title, author, pages):
#         self.title = title
#         self.author = author
#         self.pages = pages

#     def info(self):
#         print(f'Название: {self.title}\n'
#               f'Автор: {self.author}\n'
#               f'Кол-во страниц: {self.pages}')

#     def size(self):
#         if self.pages > 300:
#             print('Книга длинная')
#         else:
#             print('Книга короткая')


# book1 = Book('Шантарам', 'Дэвид Робертс', 290)
# book1.info()
# book1.size()

#2
"""
Создайте класс Студент Student с атрибутами имя name и оценка grade
Добавьте методы для установки и получения оценки студента
"""

# class Student:

#     def __init__(self, name) -> None:
#         self.name = name
#         self.grade = None

#     def set_grade(self, grade):
#         self.grade = grade

#     def get_grade(self):
#         if self.grade is None:
#             print('У студента не проставлена оценка')
#         else:
#             print(f'Оценка студента: {self.grade}')


# student1 = Student('Aziza')
# student1.get_grade()
# student1.set_grade(83)
# student1.get_grade()

#3
"""
Наследование
Создайте класс TeacherMath, TeacherLang наследуемый от Teacher,
с доп-ым атрибутом subject (предмет преподавания)
Переобпределите метод info.
"""

# class Teacher:

#     def __init__(self, name, subject):
#         self.name = name
#         self.subject = subject

#     def info(self):
#         print(f'{self.name} предмет преподавания {self.subject}')


# class TeacherMath(Teacher):
#     pass


# class TeacherLang(Teacher):
#     pass


# teacher_math = TeacherMath(name='Фибоначчи', subject='Матем')
# teacher_lang = TeacherLang(name='Гвидо Ван Россум', subject='Python')

# teacher_math.info()
# teacher_lang.info()


