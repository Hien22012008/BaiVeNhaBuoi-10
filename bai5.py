name = {
'students': [
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
],
'teachers': [
    {
        'firstName': 'Amberly', 
        'lastName': 'Calico'
    },
    {
        'firstName': 'Regine', 
        'lastName': 'Agtarap'
    }
]

}

print('List of students:')
for student in name['students']:
    print('- {} {}'.format(student['firstName'], student['lastName']))

print('List of teacher:')
for teacher in name['teachers']:
    print('- {} {}'.format(teacher['firstName'], teacher['lastName']))