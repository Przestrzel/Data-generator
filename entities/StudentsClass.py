class StudentsClass:
    def __init__(self, student_id, class_id, grade):
        self.student_id = student_id
        self.class_id = class_id
        self.grade = grade

    def get_entity_list(self):
        return [self.student_id, self.class_id, self.grade]