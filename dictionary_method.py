print("8 example of dictionary method \n")
student_profile = {'name': 'simz','age': 30, 'program course': 'python','school': 'linar','school address': 'omark bustop'}

# 1)
result = student_profile.get('name')#used to get a paticular value in the dictionary
print(''"'get method for name'"'= ', result, '\n')

# 2)
result = student_profile.pop('age')#it used remove a value and the key and return the value in the dictionary 
print(''"'pop method for age'"'=', result,  '\n')

# 3)
result = student_profile.popitem()#it used remove and return an arbitrary key value
print(''"'pop item method for the student profile'"'=',  result, '\n')

# 4)
result_1 = student_profile.update({'city_address': 'lagos',})#used to uploaad the dictionary with a new key value
print(''"'value in dict method for name'"'=', result_1, '\n')

# 5)
result = student_profile.fromkeys('school')#it used to create a new dictionary from a specific key  
print(''"'fromkey  method from school become'"'=', result, '\n')

# 6)
result = student_profile.copy()#used to copying the key and value in the dictionary
print('copy method for student profile =', result, '\n')

# 7)
result = student_profile.keys()#used to return all key in the dictionary
print('keys method for stundent profile =', result, '\n')

# 8)
result = student_profile.values()#return a list of all values in the dictionary
print('values method for stundent profile =', result, '\n')

