students = [
    {
        'firstName': 'Nikki', 
        'lastName': 'Roysden'
    },
    {
        'firstName': 'Mervin', 
        'lastName': 'Friedland'
    },
    {
        'firstName': 'Aron', 
        'lastName': 'Wilkins'
    }
]

print('List of students:')
for student in students:
    print('- {} {}'.format(student['firstName'], student['lastName']))