import csv

def people_to_csv(people, file_name):
    with open(file_name, 'w',) as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['firstname', 'lastname', 'id', 'pesel', 'birthdate', 'street', 'postcode', 'city', 'phonenumber', 'email', 'degree', 'gender'])
        for person in people:
            writer.writerow([person.first_name, person.last_name, person.id, person.pesel, person.birthdate, person.street, person.post_code, person.city, person.phone_number, person.email, person.degree, person.gender])
