# You can use the items method to get the key-value pairs as tuples and then convert them to a list of tuples.
student = {
    'first_name': 'Aman',
    'last_name': 'Mishra',
    'gender': 'Male',
    'age': 20,
    'marital_status': 'Single',
    'skills': ['Python', 'JavaScript', 'Data Analysis'],
    'country': 'India',
    'city': 'Ahmedabad',
    'address': 'Satellite'
}

# Convert the dictionary to a list of tuples
list_of_tuples = list(student.items())

# Display the list of tuples
print("List of tuples:", list_of_tuples)
