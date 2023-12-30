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

# Get the value of the 'skills' key
skills_value = student['skills']

# Check the data type of the 'skills' value
data_type_of_skills = type(skills_value)

# Display the results
print("Value of 'skills':", skills_value)
print("Data type of 'skills':", data_type_of_skills)
