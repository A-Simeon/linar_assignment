def age_calculator(name,pyear,byear):
   

    """the age calculator function is used to calculate your age and group your age group/

    it take 3 parameter

    name=str, pyear = present year, byear = birth year"""


name =input("what is your name:")

pyear =input("what the present year:")

byear =input("what is your birth year:")

age = int(pyear) - int(byear)

if age >0 and age<6:

    print("hi",name,"you are",age,"year old and you are a kid")

elif age >6 and age<13:

    print("hi",name,"you are",age,"year old and you are a kid") 

elif age >13 and age<20:
    print("hi",name,"you are",age,"year old and you are a teenage")

elif age >20 and age<35:
    print("hi",name,"you are",age,"year old and you are a young adult")

elif age >35 and age<100:
    print("hi",name,"you are",age,"year old and you are a adult")

else:    

    print("enter a valid number")



