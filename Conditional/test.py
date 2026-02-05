#if he is eligible to vote or not?
age = int(input("Enter your age: "))
citizen=input("Are you a citizen? (yes/no): ")
if age >18:
    print("age criteia passed")
    if citizen.lower()=='yes':
        print("You are eligible to vote")
    else:
        print("You are not eligible to vote")
else:
    print("You are not eligible to vote")



#anpther way
age = int(input("Enter your age: "))
citizen=input("Are you a citizen? (yes/no): ")
if age >18 and citizen.lower()=='yes':
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")

#another way
age = int(input("Enter your age: "))
citizen=input("Are you a citizen? (yes/no): ")
result="you are eligible to vote" if age>18 and citizen=="yes" else "you are not eligible to vote"
print(result)
