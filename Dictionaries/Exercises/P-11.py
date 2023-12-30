# If you want to delete the entire "student" dictionary, you can use the 'del' statement. 
student = {
    'first_name': 'John',
    'last_name': 'Doe',
    'gender': 'Male',
    'age': 20,
    'marital_status': 'Single',
    'skills': ['Python', 'JavaScript', 'Data Analysis'],
    'country': 'United States',
    'city': 'New York',
    'address': '123 Main Street'
}

print ("Before Deleting : ",student)
# Delete the entire 'student' dictionary
del student

# Trying to access 'student' after deletion will result in an error
# For example, this line will raise a NameError: name 'student' is not defined
print(student)
