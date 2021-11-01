import random

TERMS = ['Letni', 'Zimowy']
class Class:
    def __init__(self, id, course_id, teacher_id, year, type, faculty):
        self.id = id
        self.course_id = course_id
        self.teacher_id = teacher_id
        self.day = random.randint(0, 4) # 0 - Monday etc
        self.start_hour, self.end_hour = self.get_class_hours()
        self.year = year
        self.term = TERMS[random.randint(0,1)]
        self.type = type
        self.faculty = faculty
    
    def get_class_hours(self):
        start_hour = random.randint(8, 16)
        string_start_hour = str(start_hour) + ':15'
        string_end_hour = str(start_hour + random.randint(1,2)) + ':15'
        return string_start_hour, string_end_hour

    def get_entity_list(self):
        return [self.id, self.course_id, self.teacher_id, self.day, self.start_hour, self.end_hour, self.year, self.term, self.type, self.faculty]