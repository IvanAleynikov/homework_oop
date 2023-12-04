class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lr(self, lecturer, course, grades_lecturer):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades_lecturer:
                lecturer.grades_lecturer[course] += [grades_lecturer]
            else:
                lecturer.grades_lecturer[course] = [grades_lecturer]
        else:
            return 'Ошибка'

    def average_grade(self):
        total_grades = sum(sum(self.grades.values(), []))
        quantity = len(sum(self.grades.values(), []))
        return total_grades / quantity if quantity > 0 else 0

    def __str__(self):
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за лекции: {self.average_grade()}\n"
                f"Курсы в процессе изучения: {', '.join(self.courses_in_progress)}\n"
                f"Завершенные курсы: {', '.join(self.finished_courses)}")

    def __lt__(self, other):
        return self.average_grade() < other.average_grade()

    def __le__(self, other):
        return self.average_grade() <= other.average_grade()

    def __eq__(self, other):
        return self.average_grade() == other.average_grade()

    def __ne__(self, other):
        return self.average_grade() != other.average_grade()

    def __gt__(self, other):
        return self.average_grade() > other.average_grade()

    def __ge__(self, other):
        return self.average_grade() >= other.average_grade()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def  __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades_lecturer = {}

    def average_grade(self):
        total_grades = sum(sum(self.grades_lecturer.values(), []))
        quantity = len(sum(self.grades_lecturer.values(), []))
        return total_grades / quantity if quantity > 0 else 0

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_grade()}"

    def __lt__(self, other):
        return self.average_grade() < other.average_grade()

    def __le__(self, other):
        return self.average_grade() <= other.average_grade()

    def __eq__(self, other):
        return self.average_grade() == other.average_grade()

    def __ne__(self, other):
        return self.average_grade() != other.average_grade()

    def __gt__(self, other):
        return self.average_grade() > other.average_grade()

    def __ge__(self, other):
        return self.average_grade() >= other.average_grade()

class Reviewer(Mentor):
    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"


    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']

cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']

cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)

best_lecturer = Lecturer('Ruoy', 'Eman')
best_lecturer.courses_attached += ['Python']

cool_student = Student('Some', 'Buddy', 'your gender')
cool_student.courses_in_progress += ['Python']

cool_student.rate_lr(best_lecturer, 'Python', 10)
cool_student.rate_lr(best_lecturer, 'Python', 10)

# Задание 4

student1 = Student('Alice', 'Johnson', 'female')
student1.courses_in_progress = ['Python', 'OOP']
student2 = Student('Bob', 'Smith', 'male')
student2.courses_in_progress = ['Python', 'Git']

lecturer1 = Lecturer('Jim', 'Brown')
lecturer1.courses_attached = ['Python', 'OOP']
lecturer2 = Lecturer('Robin', 'Dylan')
lecturer2.courses_attached = ['Python', 'Git']

reviewer1 = Reviewer('Sam', 'Green')
reviewer1.courses_attached = ['Python', 'OOP']
reviewer2 = Reviewer('Sara', 'Lopes')
reviewer2.courses_attached = ['Python', 'Git']

reviewer1.rate_hw(student1, 'Python', 9)
reviewer1.rate_hw(student1, 'Python', 8)
reviewer2.rate_hw(student2, 'OOP', 7)
reviewer2.rate_hw(student2, 'OOP', 6)

student1.rate_lr(lecturer1, 'Python', 10)
student2.rate_lr(lecturer2, 'OOP', 9)
student1.rate_lr(lecturer1, 'Git', 8)
student2.rate_lr(lecturer2, 'OOP', 7)


print("Student 1:")
print()
print("Student 2:")
print()
print("Lecturer 1:")
print()
print("Lecturer 2:")
print()
print("Reviewer 1:")
print()
print("Reviewer 2:")
print()


lst = [student1, student2]

def awg(students, course):
    s = []
    for i in students:
        for key, value in i.grades.items():
            if key == course:
                for j in value:
                    s.append(j)
    return f'Средняя оценка студентов по предмету {course}: {sum(s) / len(s)}'

print(awg(lst, 'Python'))

lst1 = [lecturer1, lecturer2]

def awg_lec(lecturer, course):
    s = []
    for i in lecturer:
        for key, value in i.grades_lecturer.items():
            if key == course:
                for j in value:
                    s.append(j)
    return f'Средняя оценка лекторов по предмету {course}: {sum(s) / len(s)}'

print(awg_lec(lst1, 'Git'))