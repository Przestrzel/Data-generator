from datetime import datetime
import csv
from faker import Faker
import random

from services.date_service import random_date
from services.people_service import generate_people
from services.file_service import *
from entities.Course import Course
from entities.Class import Class
from entities.StudentsClass import StudentsClass
        
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
FACULTIES = ['AA', 'ETI', 'ABC', 'EEE', 'IEEE', 'DJE', 'GHE', 'PE', 'PHE', 'ZE', 'UU']
AMOUNT_OF_COURSES = AMOUNT_OF_TEACHERS
courses_id = 1
courses = []
for _ in range(AMOUNT_OF_COURSES):
    Faker.seed(random.randint(0, 1_000_000_000))
    faker = Faker()
    new_course = Course(courses_id, faker.job(), random.randint(80, 500), faker.catch_phrase(), FACULTIES[random.randint(0, len(FACULTIES) - 1)])
    courses_id += 1
    courses.append(new_course)

#Generating classes
CLASS_TYPES = ['Wyklad' , 'Cwiczenia', 'Laboratoria']
YEAR_START = 2019
AMOUNT_OF_YEARS = 2
class_id = 1
classes = []
for present_year in range(AMOUNT_OF_YEARS):
    for class_type in CLASS_TYPES:
        for course_index in range(AMOUNT_OF_COURSES):
            new_class = Class(class_id, courses[course_index].id, teachers[course_index].id, YEAR_START+present_year, class_type, courses[course_index].faculty)
            class_id += 1
            classes.append(new_class)
#Amount of classes = 3 * Amount of years * amount of courses

# Dividing students to faculties
student_faculty = []
for _ in range(AMOUNT_OF_STUDENTS):
    student_faculty.append(FACULTIES[random.randint(0, len(FACULTIES)-1)])

#TODO Genearting student's classes
GRADES = [2.0, 3.0, 3.5, 4.0, 4.5, 5.0]
student_classes = []
for student_index in range(AMOUNT_OF_STUDENTS):
    for _class in classes:
        if student_faculty[student_index] == _class.faculty:
            grade = GRADES[random.randint(0, len(GRADES) - 1)]
            new_student_class = StudentsClass(students[student_index].id, _class.id, grade)
            student_classes.append(new_student_class)

#Writing to CSV
with open('data/people.csv', 'w',) as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['firstname', 'lastname', 'id', 'pesel', 'birthdate', 'street', 'postcode', 'city', 'phonenumber', 'email', 'degree', 'gender'])
    for person in people:
        writer.writerow([person.first_name, person.last_name, person.id, person.pesel, person.birthdate, person.street, person.post_code, person.city, person.phone_number, person.email, person.degree, person.gender])


#Writing to bulks
BULK_SEPARATOR = ' | '

clear('data/students.bulk')
for student in students:
    append_to_bulk('data/students.bulk', [student.id, student.first_name, student.last_name, student.city], BULK_SEPARATOR)

clear('data/teachers.bulk')
for teacher in teachers:
    append_to_bulk('data/teachers.bulk', [teacher.id, teacher.first_name, teacher.last_name], BULK_SEPARATOR)

clear('data/courses.bulk')
for course in courses:
    append_to_bulk('data/courses.bulk', [course.id, course.name, course.max_student_amount, course.description], BULK_SEPARATOR)

clear('data/classes.bulk')
for _class in classes:
    append_to_bulk('data/classes.bulk', [_class.id, _class.course_id, _class.teacher_id, _class.day, _class.start_hour, _class.end_hour, _class.year, _class.term, _class.type, _class.faculty], BULK_SEPARATOR)

clear('data/student_classes.bulk')
for student_class in student_classes:
    append_to_bulk('data/student_classes.bulk', [student_class.student_id, student_class.class_id, student_class.grade], BULK_SEPARATOR)