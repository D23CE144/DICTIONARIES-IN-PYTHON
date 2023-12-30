# You can use the pop method to remove a specific item from the dictionary by providing its key.
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

# Remove the 'marital_status' key from the dictionary
student.pop('marital_status')

# Display the updated dictionary
print("Updated dictionary after removing 'marital_status':", student)
