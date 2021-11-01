class Course:
    
    def __init__(self, id, name, max_student_amount, description, faculty):
        self.id = id
        self.name = name
        self.max_student_amount = max_student_amount
        self.description = description
        self.faculty = faculty

    def get_entity_list(self):
        return [self.id, self.name, self.max_student_amount, self.description]