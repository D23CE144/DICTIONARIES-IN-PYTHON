# You can use the 'keys' method to get the dictionary keys and then convert them to a list. 
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

# Get the dictionary keys as a list
keys_list = list(student.keys())

# Display the list of keys
print("List of dictionary keys:", keys_list)
