print("Enter marks in 4 subjects: ")

maths = int(input("Enter your marks in Maths: "))
english = int(input("Enter your marks in English: "))
science = int(input("Enter your marks in Science: "))
social = int(input("Enter your marks in Social: "))

sum = maths + english + science + social

print("The sum of all the marks is: ", sum)

percent = (sum/400)*100

print(f"Percentage of marks: {percent} %")