age = int(input("Please enter your age: "))

if age >= 0 and age <= 12:
    print("You are classified as a child!")
elif age >= 13 and age <= 19:
    print("You are classified as a Teen!")
elif age >= 20 and age <= 64:
    print("You are classified as an Adult!")
elif age > 65:
    print("You are classified as a Senior citizen!")
else:
    print("You are unclassified! proably because you put a fake a age or a negative age")     
