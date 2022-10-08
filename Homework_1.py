class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.course_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.course_in_progress and course in lecturer.course_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __average_grade(self):
        sum_grades = 0
        count = 0
        for course_grade in self.grades.values():
            for grade in course_grade:
                count += 1
                sum_grades += int(grade)
        if count == 0:
            return 'Оценок еще нет!'
        else:
            result = sum_grades / count
        return round(result, 1)

    def __lt__(self, other):
        if not isinstance(other, Student):
            return f'{other.name} {other.surname} - Такого студента нет!'
        return self.__average_grade() < other.__average_grade()

    def __str__(self):
        res = f'Имя: {self.name}\n' \
              f'Фамилия: {self.surname}\n' \
              f'Средняя оценка за домашние задания: {self.__average_grade()}\n' \
              f'Курсы в процессе изучения: {", ".join(self.course_in_progress)}\n' \
              f'Завершенные курсы: {", ".join(self.finished_courses)}'
        return res


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.course_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __average_grade(self):
        sum_grades = 0
        count = 0
        for course_grade in self.grades.values():
            for grade in course_grade:
                count += 1
                sum_grades += int(grade)
        if count == 0:
            return 'Оценок еще нет!'
        else:
            result = sum_grades / count
        return round(result, 1)

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return f'{other.name} {other.surname} - Такого лектора нет!'
        return self.__average_grade() < other.__average_grade()

    def __str__(self):
        res = f'Имя: {self.name}\n' \
              f'Фамилия: {self.surname}\n' \
              f'Средняя оценка за лекции: {self.__average_grade()}'
        return res


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.course_attached and course in student.course_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name}\n' \
              f'Фамилия: {self.surname}'
        return res


student_1 = Student('Jon', 'Jones', 'man')
student_2 = Student('Liza', 'Clark', 'women')
student_1.finished_courses += ['Введение в программирование']
student_1.finished_courses += ['Git']
student_1.course_in_progress += ['Python']
student_2.finished_courses += ['Введение в программирование']
student_2.finished_courses += ['Git']
student_2.course_in_progress += ['C++']

lecturer_1 = Lecturer('Ivan', 'Ivanov')
lecturer_2 = Lecturer('Petr', 'Petrov')
lecturer_1.course_attached += ['Python']
lecturer_2.course_attached += ['C++']

reviewer_1 = Reviewer('Pavel', 'Sidorov')
reviewer_2 = Reviewer('Anna', 'Smirnova')
reviewer_1.course_attached += ['Python']
reviewer_2.course_attached += ['C++']

student_1.rate_lecture(lecturer_1, 'Python', 10)
student_1.rate_lecture(lecturer_1, 'Python', 9)
student_2.rate_lecture(lecturer_2, 'C++', 9)
student_2.rate_lecture(lecturer_2, 'C++', 8)

reviewer_1.rate_hw(student_1, 'Python', 9)
reviewer_1.rate_hw(student_1, 'Python', 8)
reviewer_2.rate_hw(student_2, 'C++', 8)
reviewer_2.rate_hw(student_2, 'C++', 7)

list_students = [student_1, student_2]
list_lecturers = [lecturer_1, lecturer_2]


def average_all_students(students, course):
    sum_grade = 0
    count = 0
    for student in students:
        if course in list(student.grades.keys()):
            for grade in student.grades[course]:
                sum_grade += int(grade)
                count += 1
    if count == 0:
        return 'По данному курсу студенты оценок не получали!'
    else:
        result = sum_grade / count
        return result


def average_all_lecturers(lecturers, course):
    sum_grade = 0
    count = 0
    for lecturer in lecturers:
        if course in list(lecturer.grades.keys()):
            for grade in lecturer.grades[course]:
                sum_grade += int(grade)
                count += 1
    if count == 0:
        return 'По данному курсу лекторы оценок не получали!'
    else:
        result = sum_grade / count
        return result


print(student_1)
print(student_2)
print(student_1 < student_2)
print(student_2 < student_1)
print(lecturer_1)
print(lecturer_2)
print(lecturer_1 < lecturer_2)
print(lecturer_2 < lecturer_1)
print(reviewer_1)
print(reviewer_2)
print(average_all_students(list_students, 'Python'))
print(average_all_lecturers(list_lecturers, 'C++'))
