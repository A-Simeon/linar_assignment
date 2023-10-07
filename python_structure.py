print("calculating quadratic equation with python")
# Input dimensions for length, width and height
height = 12  # Constant room height in feet (feet given)
length = float(input("Enter the length of room 1 (in feet) "))

width = float(input("Enter the width of  room 1 (in feet) "))

length = float(input("Enter the length of room 2 (in feet) "))
width = float(input("Enter the width of  room 2(in feet) "))

length = float(input("Enter the length of room 3(in feet) "))
width = float(input("Enter the width of  room 3(in feet) "))

length = float(input("Enter the length of room 4(in feet) "))
width = float(input("Enter the width of  room 4(in feet) "))

length = float(input("Enter the length of toilet(in feet) "))
width = float(input("Enter the width of  toilet(in feet) "))

import math
#FOR BLOCK A
#convert from feet to inches
brick_length_A = 1.25
brick_width_A = 0.5
brick_height_A = 0.75

#for room 1 
#for length
wall_BL= length // (brick_length_A)
wall_BH = height // (brick_height_A)
TB_wall_BL= wall_BL *wall_BH
length_FB = TB_wall_BL**2
#for width                 
wall_BW=width // (brick_width_A)
wall_BH = height //  (brick_height_A)
TB_wall_BW = wall_BW * wall_BH
width_FB = TB_wall_BW**2

TB_for_room_1 = length_FB * width_FB
"""where  BL =  block length
                 BW = block width
                 BH =  block height
                 TB =  total block
                  FB =  front and back"""                                                                                                #for room 2
#for length
wall_BL= length // (brick_length_A)
wall_BH = height // (brick_height_A)
TB_wall_BL = wall_BL *wall_BH
length_FB = TB_wall_BL**2       
#for width           
wall_BW= width //(brick_width_A)
wall_BH = height // (brick_height_A)
TB_wall_BW= wall_BW * wall_BH
width_FB = TB_wall_BW**2

TB_for_room_2 = length_FB * width_FB
"""where  BL = block length
                 BW = block width
                 BH = block height
                 TB = total block
                  FB = front and back"""
                  
#for room 3
#for length
wall_BL= length // (brick_length_A)
wall_BH = height // (brick_height_A)
TB_wall_BL= wall_BL *wall_BH
length_FB = TB_wall_BL**2
#for width                 
wall_BW= width // (brick_width_A)
wall_BH = height * (brick_height_A)
TB_wall_BW= wall_BW * wall_BH
width_FB = TB_wall_BW**2

TB_for_room_3 = length_FB * width_FB
"""where  BL = block length
                 BW = block width
                 BH = block height
                 TB = total block
                  FB = front and back"""
                                  
#for room 4
#for length
wall_BL= length // (brick_length_A)
wall_BH = height // (brick_height_A)
TB_wall_BL= wall_BL *wall_BH
length_FB = TB_wall_BL**2
#for width                  
wall_BW= width // (brick_width_A)
wall_BH = height // (brick_height_A)
TB_wall_BW= wall_BW * wall_BH
width_FB = TB_wall_BW**2

TB_for_room_4 = length_FB * width_FB
"""where  BL = block length
                 BH = block height
                 BW = block width
                 TB = total block
                  FB = front and back"""
#for toilet
#for length
wall_BL= length // (brick_length_A)
wall_BH = height // (brick_height_A)
TB_wall_BL= wall_BL * wall_BH
length_FB = TB_wall_BL**2             
#for width               
wall_BW= width // (brick_width_A)
wall_BH = height // (brick_height_A)
TB_wall_BW = wall_BW * wall_BH
width_FB = TB_wall_BW**2

TB_for_TOI = length_FB * width_FB
"""where  BL = block length 
                 BH = block height
                 BW = block width 
                 TOI =Toilet
                  TB = total block
                   FB = front and back"""
                  
                  
                  
                  
#FOR BLOCK B                  
#convert from feet to inches
brick_length_B = 1.6666666667
brick_width_B = 0.8333333333
brick_height_B = 1

#for room 1 
#for length
wall_BL = length // (brick_length_B)
wall_BH = height // (brick_height_B)
TB_wall_BL= wall_BL *wall_BH
length_FB = TB_wall_BL**2
#for width                 
wall_BW =width // (brick_width_B)
wall_BH = height //  (brick_height_B)
TB_wall_BW = wall_BW * wall_BH
width_FB = TB_wall_BW**2

TB_for_room_1 = length_FB * width_FB
"""where  BL =  block length
                 BW = block width
                 BH =  block height
                 TB =  total block
                  FB =  front and back"""                                                                                                #for room 2
#for length
wall_BL= length // (brick_length_B)
wall_BH = height // (brick_height_B)
TB_wall_BL= wall_BL *wall_BH
lenght_FB = TB_wall_BL**2       
#for width           
wall_BW = width // (brick_width_B)
wall_BH = height // (brick_height_B)
TB_wall_BW = wall_BW * wall_BH
width_FB = TB_wall_BW**2

TB_for_room_2 = length_FB * width_FB
"""where  BL = block length
                 BW = block width
                 BH = block height
                 TB = total block
                  FB = front and back"""
                  
#for room 3
#for length
wall_BL= length // (brick_length_B)
wall_BH = height // (brick_height_B)
TB_wall_BL= wall_BL *wall_BH
length_FB = TB_wall_BL**2
#for width                 
wall_BW = width // (brick_width_B)
wall_BH = height // (brick_height_B)
TB_wall_BW = wall_BW * wall_BH
width_FB = TB_wall_BW**2

TB_for_room_3 = length_FB * width_FB
"""where  BL = block length
                 BW = block width
                 BH = block height
                 TB = total block
                  FB = front and back"""
                                  
#for room 4
#for length
wall_BL= length // (brick_length_B)
wall_BH = height // (brick_height_B)
TB_wall_BL = wall_BL *wall_BH
length_FB = TB_wall_BL**2
#for width                  
wall_BW = width // (brick_width_B)
wall_BH = height // (brick_height_B)
TB_wall_BW = wall_BW * wall_BH
width_FB = TB_wall_BW**2

TB_for_room_4 = length_FB * width_FB
"""where  BL = block length
                 BH = block height
                 BW = block width
                 TB = total block
                  FB = front and back"""      
#for toilet
#for length
wall_BL= length // (brick_length_B)
wall_BH = height // (brick_height_B)
TB_wall_BL= wall_BL * wall_BH
length_FB = TB_wall_BL**2             
#for width               
wall_BW= width // (brick_width_B)
wall_BH = height // (brick_height_B)
TB_wall_BW= wall_BW * wall_BH
width_FB = TB_wall_BW**2
TB_for_TOI = length_FB * width_FB
"""where  BL = block length 
                 BH = block height
                 BW = block width 
                 TOI =Toilet
                 TB = total block
                  FB = front and back"""
                  
                  
                  
#cost of block A
cost_of_block_A = 600
cost_of_block_B = 1000                   
 
#cost for block A (room and toilet)
cost_of_block_A_for_room_1 = cost_of_block_A * TB_for_room_1          
cost_of_block_A_for_room_2 = cost_of_block_A * TB_for_room_2
cost_of_block_A_for_room_3= cost_of_block_A * TB_for_room_3
cost_of_block_A_for_room_4 = cost_of_block_A * TB_for_room_4
cost_of_block_A_for_TOI = cost_of_block_A * TB_for_TOI   

#cost for block B (room and toilet)
cost_of_block_B_for_room_1 = cost_of_block_B * TB_for_room_1
cost_of_block_B_for_room_2 = cost_of_block_B * TB_for_room_2
cost_of_block_B_for_room_3 = cost_of_block_B * TB_for_room_3
cost_of_block_B_for_room_4 = cost_of_block_B * TB_for_room_4
cost_of_block_B_for_TOI= cost_of_block_B * TB_for_TOI


#result
#for total number for A
print("Total number of block A needed for room 1", int(TB_for_room_1))
print("Total number of block A needed for room 2", int(TB_for_room_2))
print("Total number of block A needed for room 3", int(TB_for_room_3))
print("Total number of block A needed for room 4", int(TB_for_room_4))
print("Total number of block A needed for toilet", int(TB_for_TOI))

#for total cost for A
print("Total cost of block A for room 1: ₦", cost_of_block_A_for_room_1)
print("Total cost of block A for room 2: ₦", cost_of_block_A_for_room_2)
print("Total cost of block A for room 3: ₦", cost_of_block_A_for_room_3)
print("Total cost of block A for room 4: ₦", cost_of_block_A_for_room_4)
print("Total cost of block A for toilet: ₦",cost_of_block_A_for_TOI)    
           
#for total number for B
print("Total number of block B needed for room 1", int(TB_for_room_1))
print("Total number of block B needed for room 2", int(TB_for_room_2))
print("Total number of block B needed for room 3", int(TB_for_room_3))
print("Total number of block B needed for room 4", int(TB_for_room_4))
print("Total number of block B needed for toilet", int(TB_for_TOI))            

 #for total cost for B
print("Total cost of block B for room 1: ₦", cost_of_block_B_for_room_1)
print("Total cost of block B for room 2: ₦", cost_of_block_B_for_room_2)
print("Total cost of block B for room 3: ₦", cost_of_block_B_for_room_3)
print("Total cost of block ,B for room 4: ₦", cost_of_block_B_for_room_4)
print("Total cost of block Bfor toilet: ₦", cost_of_block_B_for_TOI)                                                                                                                                                                                                                                                                                                                           