class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lector, course, grade):
        if isinstance(lector, Lecture) and course in lector.courses_attached and course in self.courses_in_progress:
            if course in lector.grades:
                lector.grades[course] += [grade]
            else:
                lector.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __eq__(self, student):
        return print(average_grade_student(self) > average_grade_student(student))

    def __str__(self, student):
        return print(f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {average_grade_student(student)}\nКурсы в процессе изучения: {', '.join(self.courses_in_progress)}\nЗавершенные курсы: {', '.join(self.finished_courses)}')

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
 

class Lecture(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __eq__(self, lector):
        return print(average_grade_student(self) > average_grade_student(lector))

    def __str__(self, lector):
        return print(f'Имя {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {average_grade_lector(lector)}')

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self, reviewer):
        return print(f'Имя {self.name}\nФамилия: {self.surname}')

def average_grade_student(student):
    sum_grade = 0
    for i in student.grades.values():
        sum_grade += sum(i)
    quantity_grade = 0
    for i in student.grades.values():
        quantity_grade += len(i)
    return sum_grade / quantity_grade

def average_grade_lector(lector):
    sum_grade = 0
    for i in lector.grades.values():
        sum_grade += sum(i)
    quantity_grade = 0
    for i in lector.grades.values():
        quantity_grade += len(i)
    return sum_grade / quantity_grade

student_1 = Student('Artem', 'Tn', 'Male')
student_1.courses_in_progress += ['Python']
student_1.courses_in_progress += ['Git']
student_1.finished_courses += ['Frontend']
student_1.finished_courses += ['Backend']

student_2 = Student('Alina', 'Bv', 'Female')
student_2.courses_in_progress += ['DevOps']
student_2.courses_in_progress += ['Analitika']
student_2.finished_courses += ['Python']
student_2.finished_courses += ['Git']

lector_1 = Lecture('Nikita', 'Romanovich')
lector_1.courses_attached += ['Python']
lector_1.courses_attached += ['Git']

lector_2 = Lecture('Vika', 'Kolosova')
lector_2.courses_attached += ['DevOps']
lector_2.courses_attached += ['Analitika']

student_1.rate_lecturer(lector_1, 'Python', 10)
student_1.rate_lecturer(lector_1, 'Python', 10)
student_1.rate_lecturer(lector_1, 'Git', 9)
student_1.rate_lecturer(lector_1, 'Git', 4)

student_2.rate_lecturer(lector_2, 'DevOps', 10)
student_2.rate_lecturer(lector_2, 'Analitika', 9)
student_2.rate_lecturer(lector_2, 'Analitika', 7)
student_2.rate_lecturer(lector_2, 'DevOps', 5)

reviewer_1 = Reviewer('Polina', 'Pospelova')
reviewer_1.courses_attached += ['Python']
reviewer_1.courses_attached += ['Git']
reviewer_1.rate_hw(student_1, 'Python', 10)
reviewer_1.rate_hw(student_1, 'Python', 3)
reviewer_1.rate_hw(student_1, 'Git', 7)
reviewer_1.rate_hw(student_1, 'Git', 10)

reviewer_2 = Reviewer('Renata', 'Kostyunina')
reviewer_2.courses_attached += ['DevOps']
reviewer_2.courses_attached += ['Analitika']
reviewer_2.rate_hw(student_2, 'DevOps', 9)
reviewer_2.rate_hw(student_2, 'DevOps', 5)
reviewer_2.rate_hw(student_2, 'Analitika', 2)
reviewer_2.rate_hw(student_2, 'Analitika', 7)

student_1.__str__(student_1)
student_2.__str__(student_2)
student_1.__eq__(student_2)

lector_1.__str__(lector_1)
lector_2.__str__(lector_2)
lector_1.__eq__(lector_2)

reviewer_1.__str__(reviewer_1)
reviewer_2.__str__(reviewer_2)