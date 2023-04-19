from math import sqrt

x = [10.1,0.4,6.9,4.2,14.1,15.9]
y = [17.7,3.1,9.0,2.7,41.5,33.3]
cities = ['Elabro','Nutunyu','Barimba','Duduth','Tromsu','Pranho'] 

print("City List:")
for i in range(len(cities)):
    print (f"{cities[i]} : (x = {x[i]}, y = {y[i]})")

print("\nShortest Distance:")
min_pair = [0,1]
for i in range(len(cities)-1):  
    for j in range(i+1, len(cities)):
        location1 = (x[i] - x[j]) ** 2
        location2 = (y[i] - y[j]) ** 2
        new_distance =  sqrt(location1 + location2) 

        checkPair1 = (x[min_pair[0]] - x[min_pair[1]]) ** 2
        checkPair2 = (y[min_pair[0]] - y[min_pair[1]]) ** 2
        short_distance = sqrt(checkPair1 + checkPair2)

        if new_distance < short_distance:
            min_pair[0] = i
            min_pair[1] = j
            
print("The two cities that are closest to each other are:", cities[min_pair[0]], "and", cities[min_pair[1]])
        