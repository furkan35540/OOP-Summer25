# List of students, where each student is a dictionary
students = [
    {
        'first_name': 'Ahmet',
        'second_name': 'Arda',
        'last_name': 'Balkaya',
        'nationality': 'Turkish',
        'index_number': 35535,
        'starting_date': '10/10/2024',
        'courses': ['english', 'maths']
    },
    {
        'first_name': 'Yagiz',
        'second_name': 'Mehmet',
        'last_name': 'Findikli',
        'nationality': 'Turkish',
        'index_number': 45678,
        'starting_date': '12/01/2023',
        'courses': ['history', 'biology']
    },
    {
        'first_name': 'Youssef',
        'second_name': 'Sofyan',
        'last_name': 'En-nesyri',
        'nationality': 'Moroccan',
        'index_number': 12345,
        'starting_date': '08/09/2022',
        'courses': ['chemistry', 'physics']
    }
]

for student in students:
    full_name = f"{student['first_name']} {student['second_name']} {student['last_name']}"
    print(f"Name: {full_name}, Index: {student['index_number']}")
