class Student:
    def __init__(self, first_name, second_name, last_name, nationality, index_number, starting_date, courses):
        self.first_name = first_name
        self.second_name = second_name
        self.last_name = last_name
        self.nationality = nationality
        self.index_number = index_number
        self.starting_date = starting_date
        self.courses = courses


student1 = Student(
    first_name='Ahmet',
    second_name='Arda',
    last_name='Balkaya',
    nationality='Turkish',
    index_number=35535,
    starting_date='10/10/2024',
    courses=['english', 'maths']
)


print(student1.first_name)
print(student1.second_name)
print(student1.last_name)
print(student1.nationality)
print(student1.index_number)
print(student1.starting_date)
print(student1.courses)
