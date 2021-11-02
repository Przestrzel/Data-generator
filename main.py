from datetime import datetime
import random

from services.people_service import generate_people
from services.csv_service import people_to_csv

from services.entities_service import generate_courses
from services.entities_service import generate_classes
from services.entities_service import generate_student_classes
from services.entities_service import entities_to_bulk
from services.entities_service import FACULTIES

### Generating first snapshot
AMOUNT_OF_STUDENTS = 30
students_id = 10_000
student_startbirth = datetime.strptime('1/1/1990 1:30 PM', '%m/%d/%Y %I:%M %p')
student_endbirth = datetime.strptime('1/1/2003 4:50 AM', '%m/%d/%Y %I:%M %p')

AMOUNT_OF_TEACHERS = 10
teachers_id = 100
teacher_startbirth = datetime.strptime('1/1/1960 1:30 PM', '%m/%d/%Y %I:%M %p')
teacher_endbirth = datetime.strptime('1/1/1995 4:50 AM', '%m/%d/%Y %I:%M %p')

students = generate_people(student_startbirth, student_endbirth, AMOUNT_OF_STUDENTS, students_id, 0)
teachers = generate_people(teacher_startbirth, teacher_endbirth, AMOUNT_OF_TEACHERS, teachers_id, 2)
people = students + teachers

AMOUNT_OF_COURSES = AMOUNT_OF_TEACHERS
courses = generate_courses(AMOUNT_OF_COURSES)

AMOUNT_OF_YEARS = 2 # amount of years to simulate
YEAR_START = 2019
classes = generate_classes(courses, teachers, AMOUNT_OF_YEARS, YEAR_START)
YEAR_START += AMOUNT_OF_YEARS
# Dividing students to faculties
students_faculty = []
for _ in range(AMOUNT_OF_STUDENTS):
    students_faculty.append(FACULTIES[random.randint(0, len(FACULTIES)-1)])

student_classes = generate_student_classes(students, classes, students_faculty)

people_to_csv(people, 'data/first_snapshot/people.csv')

entities_to_bulk('data/first_snapshot/students.bulk', students, True)
entities_to_bulk('data/first_snapshot/teachers.bulk', teachers)
entities_to_bulk('data/first_snapshot/courses.bulk', courses)
entities_to_bulk('data/first_snapshot/classes.bulk', classes)
entities_to_bulk('data/first_snapshot/student_classes.bulk', student_classes)


### Generating second snapshot
AMOUNT_OF_NEW_STUDENTS = int(AMOUNT_OF_STUDENTS / 5)
AMOUNT_OF_NEW_TEACHERS = int(AMOUNT_OF_TEACHERS / 5)

new_students = generate_people(student_startbirth, student_endbirth, AMOUNT_OF_NEW_STUDENTS, students_id + len(students), 0)
new_teachers = generate_people(teacher_startbirth, teacher_endbirth, AMOUNT_OF_NEW_TEACHERS, teachers_id + len(teachers), 2)
new_people = new_students + new_teachers

#! Changing last_name for requirements of datawarehouse
all_students = students + new_students
for _ in range(int((AMOUNT_OF_STUDENTS + AMOUNT_OF_NEW_STUDENTS) / 10)):
    all_students[random.randint(0, AMOUNT_OF_STUDENTS + AMOUNT_OF_NEW_STUDENTS - 1)].last_name = 'Nowak'

for _ in range(int((AMOUNT_OF_STUDENTS + AMOUNT_OF_NEW_STUDENTS) / 5)):
    all_students[random.randint(0, AMOUNT_OF_STUDENTS + AMOUNT_OF_NEW_STUDENTS - 1)].degree = 'Inzynier'

AMOUNT_OF_NEW_COURSES = AMOUNT_OF_NEW_TEACHERS
new_courses = generate_courses(AMOUNT_OF_NEW_COURSES, 1 + len(courses))

AMOUNT_OF_YEARS = 1 # amount of years to simulate
new_classes = generate_classes(new_courses, new_teachers, AMOUNT_OF_YEARS, YEAR_START, 1 + len(classes))

new_students_faculty = []
for _ in range(AMOUNT_OF_NEW_STUDENTS):
    new_students_faculty.append(FACULTIES[random.randint(0, len(FACULTIES)-1)])

#old student go to new classes
prev_student_classes = generate_student_classes(students, new_classes, students_faculty)
#new student go to previous classes
new_student_classes = generate_student_classes(new_students, classes, new_students_faculty)

people_to_csv(people + new_people, 'data/second_snapshot/people.csv')

entities_to_bulk('data/second_snapshot/students.bulk', students + new_students, True)
entities_to_bulk('data/second_snapshot/teachers.bulk', teachers + new_teachers)
entities_to_bulk('data/second_snapshot/courses.bulk', courses + new_courses)
entities_to_bulk('data/second_snapshot/classes.bulk', classes + new_classes)
entities_to_bulk('data/second_snapshot/student_classes.bulk', student_classes + new_student_classes + prev_student_classes)