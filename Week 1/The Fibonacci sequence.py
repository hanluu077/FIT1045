'''
FIT1045 Python Week 1 

Task: Create the expected Output using 'The Fibonacci Sequence'
F 0 = 0
F 1 = 1
F 2 = 1
F 3 = 2
F 4 = 3
F 5 = 5
F 6 = 8
F 7 = 13
F 8 = 21
'''
# Create Variables
n1 = 0                      
n2 = 1                          
index = 2                    # Skip Index 0 and 1, reffer to line 21
max = 9 

# Index 0, and 1	
print("F 0 =", n1)
print("F 1 =", n2)

# The Fibonacci Sequence from index 2 and onwards
while index < max: 	 
    result = n1 + n2   
    print("F", index, "=", result)
    index = index + 1
    n1 = n2
    n2 = result