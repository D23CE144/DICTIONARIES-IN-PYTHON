# The 'extend' method to add two additional skills ('Machine Learning' and 'Communication') to the existing list of skills.
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

# Add one or two skills to the existing list of skills
student['skills'].extend(['Machine Learning', 'Communication'])

# Display the updated 'skills' values
print("Updated 'skills' values:", student['skills'])