# You can use the 'values' method to get the dictionary values and then convert them to a list. 
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

# Get the dictionary values as a list
values_list = list(student.values())

# Display the list of values
print("List of dictionary values:", values_list)
