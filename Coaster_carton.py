
# Function to calculate the total amount
username = input("enter your name")
print("Hi",username,"Welcome to simz Coaster Biscuit Depot!")
    
# Ask the customer for input
coaster_biscuit_type = input("Enter the biscuit type (20 or 50): ")
carton_quantity = int(input("Enter the carton quantity(eg 1,2): "))
carton_size = input("Enter the size (small, medium, or large): ")
    
carton_size_20_cost= {
    "small": 4000,
    "medium": 5500,
    "large": 7000
}

carton_size_50_cost = {
    "small": 4000,
    "medium": 5500,
    "large": 7000
} 


    # Calculate the total amount
if coaster_biscuit_type == "20":
    cost_per_carton = carton_size_20_cost.get(carton_size)
elif coaster_biscuit_type == "50":
    cost_per_carton = carton_size_20_cost.get(carton_size)
else:
    print("Invalid biscuit type!")
        
if cost_per_carton:
   total_amount = cost_per_carton * carton_quantity    
   print("hi",username,"your total amount is",total_amount)
