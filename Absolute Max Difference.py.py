#  Task1: Takes a list of numbers and find the absoulte max Differences
# For example, for the input [10.1,35.7,3.3,4.2,14.1,-15.9], the output should be 51.6 because 
# ∣ 35.7 − (−15.9) ∣ = 51.6

findAbsMax = True

myStringInput = input("Please enter a list of numbers: ")
myNumList = myStringInput.split(',') #becomes a list 

if findAbsMax:
    maxDif = 0.0
    for i in range(len(myNumList)-1): #stop at the second last 
        for j in range(i+1, len(myNumList)): #shift in one position forward 
            checkMax = abs(float(myNumList[i]) - float(myNumList[j]))
            if maxDif < checkMax:
                maxDif = checkMax
    print("The Max Dif:", maxDif)


        







# output = input("The maximum absolute difference is: out")

