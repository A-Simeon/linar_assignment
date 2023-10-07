name = input("enter your name")
print("hello", name, "welcome to simz calculator")
def add_number(x, y):
    return x + y
    
def sub_number(x, y):
    sub_value = x - y
    return sub_valu

def div_number(x, y):
    div_value = x / y
    return  div_value

def mul_number(x, y):
    mul_value = x * y
    return  mul_value

def exp_number(x, y):
    exp_value = x ** y
    return exp_value


value_1 =((input("enter your first value")))
operator =((input("enter the selected operator(+ - / * **(for exponential) )")))
value_2 =(input("enter your second value"))
print(value_1, operator, value_2)
if operator== "+":
    print(add_number(x=value_1, y=value_2))
elif operator == "-":
    print(sub_number(x=value_1, y=value_2))
elif operator == "/":
    print(sub_number(x=value_1, y=value_2))
elif operator == "*":
    print(mul_number(x=value_1, y=value_2))
elif operator == "**":
    print(exp_number(x=value_1, y=value_2))
else:
    print("invalid score")     
