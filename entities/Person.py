import random
import pandas as pd
import csv
from faker import Faker

class Person:
    def __init__(self, first_name, last_name, birthdate, pesel, email, id, degree, city, postal_code, street):
        self.first_name = first_name
        self.last_name = last_name
        self.id = id
        self.pesel = pesel
        self.birthdate = birthdate
        self.street = street
        self.post_code = postal_code
        self.city = city
        self.phone_number = self.random_phone_number()
        self.email = email
        self.degree = degree
        self.gender = ''
        if first_name[len(first_name)-1] == 'a' or first_name == 'Nicole':
            self.gender = 'kobieta'
        else:
            self.gender = 'mezczyzna'

    def get_entity_list(self):
        return [self.id, self.first_name, self.last_name] #If student add city!
        
    def random_phone_number(self):
        phone_number = ''
        for i in range(3):
            phone_number += str(random.randint(300, 999))
        
        return phone_number