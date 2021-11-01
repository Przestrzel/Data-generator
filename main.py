from datetime import datetime
import csv
import random

from services.people_service import generate_people
from services.csv_service import people_to_csv

from services.entities_service import generate_courses
from services.entities_service import generate_classes
from services.entities_service import generate_student_classes
from services.entities_service import entities_to_bulk
from services.entities_service import FACULTIES
        
#Generating people
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

#Generating courses
AMOUNT_OF_COURSES = AMOUNT_OF_TEACHERS
courses = generate_courses(AMOUNT_OF_COURSES)

#Generating classes
AMOUNT_OF_YEARS = 2 # amount of years to simulate
classes = generate_classes(courses, teachers, AMOUNT_OF_YEARS)

# Dividing students to faculties
students_faculty = []
for _ in range(AMOUNT_OF_STUDENTS):
    students_faculty.append(FACULTIES[random.randint(0, len(FACULTIES)-1)])

#Genearting student's classes
student_classes = generate_student_classes(students, classes, students_faculty)

people_to_csv(people, 'data/first_snapshot/people.csv')

#Writing to bulks
entities_to_bulk('data/first_snapshot/students.bulk', students, True)
entities_to_bulk('data/first_snapshot/teachers.bulk', teachers)
entities_to_bulk('data/first_snapshot/courses.bulk', courses)
entities_to_bulk('data/first_snapshot/classes.bulk', classes)
entities_to_bulk('data/first_snapshot/student_classes.bulk', student_classes)
