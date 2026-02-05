#wap to calculate newtons gravitational force between two objects
m1=float(input("Enter mass of first object (in kg): "))
m2=float(input("Enter mass of second object (in kg): "))
r=float(input("Enter distance between the centers of the two objects (in meters): "))
G=6.67430e-11  # gravitational constant in m^3 kg^-1 s^-2
force=G*(m1*m2)/(r**2)
print(f"The gravitational force between the two objects is {force} Newtons")


#another way using conditional expression
m1=float(input("Enter mass of first object (in kg): "))
m2=float(input("Enter mass of second object (in kg): "))
r=float(input("Enter distance between the centers of the two objects (in meters): "))
G=6.67430e-11  # gravitational constant in m^3 kg^-1 s^-2
force=G*(m1*m2)/(r**2)
result=f"The gravitational force between the two objects is {force} Newtons" if r!=0 else "Distance cannot be zero"
print(result)

