length1 = float(input("Enter the length of area 1 : "))
width1 = float(input("Enter the width of area 1 : "))

length2 = float(input("Enter the length of area 2 : "))
width2 = float(input("Enter the width of area 2 : "))
 
Area1 = width1 * length1
Area2 = width2 * length2

if Area1 > Area2 :
    print("area 1 is greater than area 2")
elif Area2 > Area1 : 
    print("area 1 is greater than area 2")
elif Area1 == Area2 :
    print("it's have same value")
    
print(f"area 1 {Area1} and area {Area2}")