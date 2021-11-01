from faker import Faker
import random
from entities.Course import Course
from entities.Class import Class
from entities.StudentsClass import StudentsClass
from services.file_service import *

FACULTIES = ['AA', 'ETI', 'ABC', 'EEE', 'IEEE', 'DJE', 'GHE', 'PE', 'PHE', 'ZE', 'UU']
def generate_courses(AMOUNT_OF_COURSES, course_id = 1):
    courses = []
    for _ in range(AMOUNT_OF_COURSES):
        Faker.seed(random.randint(0, 1_000_000_000))
        faker = Faker()
        new_course = Course(course_id, faker.job(), random.randint(80, 500), faker.catch_phrase(), FACULTIES[random.randint(0, len(FACULTIES) - 1)])
        course_id += 1
        courses.append(new_course)

    return courses    

def generate_classes(courses, teachers, AMOUNT_OF_YEARS, YEAR_START, class_id = 1):
    CLASS_TYPES = ['Wyklad' , 'Cwiczenia', 'Laboratoria']
    classes = []
    for present_year in range(AMOUNT_OF_YEARS):
        for class_type in CLASS_TYPES:
            for course_index in range(len(courses)):
                new_class = Class(class_id, courses[course_index].id, teachers[course_index].id, YEAR_START+present_year, class_type, courses[course_index].faculty)
                class_id += 1
                classes.append(new_class)
    
    return classes

def generate_student_classes(students, classes, students_faculty):
    GRADES = [2.0, 3.0, 3.5, 4.0, 4.5, 5.0]
    student_classes = []
    for student_index in range(len(students)):
        for _class in classes:
            if students_faculty[student_index] == _class.faculty:
                grade = GRADES[random.randint(0, len(GRADES) - 1)]
                new_student_class = StudentsClass(students[student_index].id, _class.id, grade)
                student_classes.append(new_student_class)
    
    return student_classes

BULK_SEPARATOR = ' | '
def entities_to_bulk(file_name, entities, isStudent = False):
    clear(file_name)
    for entity in entities:
        append_to_bulk(file_name, entity.get_entity_list() + [entity.city] if isStudent else entity.get_entity_list(), BULK_SEPARATOR)