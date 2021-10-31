from faker import Faker
import random
from entities.Person import Person
from services.date_service import random_date

DEGREES = ['Student', 'Inzynier', 'Magister', 'Doktor']

def generate_people(start_birth, end_birth, amount, id_start, degree_start):
    id = id_start
    people_list = []
    for _ in range(amount):
        random_birthdate = random_date(start_birth, end_birth)
        shortend_birthdate = str(random_birthdate)[:10]

        Faker.seed(random.randint(0, 1_000_000_000))
        faker = Faker('pl_PL')
        person = Person(faker.first_name(), faker.last_name(), shortend_birthdate, faker.pesel(random_birthdate), faker.free_email(),id, DEGREES[random.randint(degree_start, degree_start + 1)], faker.city(), faker.postcode(), faker.street_address())
        id += 1
        people_list.append(person)
    
    return people_list