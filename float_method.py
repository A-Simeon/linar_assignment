#float method
number_string = 3.114
result = number_string.hex()#to return a hexadecimal value from the string value
print(result)


x = 4.88
y = 2.22
result = x.__floordiv__(y)#it divide the result(x/y) and then return the answer in floor value 
print(result)

a =10/4
result = a.__floor__()#it change the interger value to floor value
print(result)

x = 100.0
result = x.__round__()#to round up a value
print(result)


a = 45/2
result = a.__add__(2.5)#for addition
print(result)