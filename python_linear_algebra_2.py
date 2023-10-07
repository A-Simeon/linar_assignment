L = float(input("enter value for L: "))
F = float(input("enter value for F: "))
w = float(input("enter value for w: "))
S = float(input("enter value for S: "))
n = float(input("enter value for n: "))


#for the result
Y = (L-F)**w*(S*L/F+(20/F)**n) /(20**w) - (F)**1/2
result = Y
print("Y =",result)

