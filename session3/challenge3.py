num = int(input("Please enter a number between 0 and 100: "))
grade = ""

if num < 0 or num > 100:
    grade = "Does not exist"
elif num >= 90:
    grade = "A"
elif num >= 80:
    grade = "B"
elif num >= 70:
    grade = "C"
elif num >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Your grade is: {grade}")
