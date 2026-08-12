marks = int(input("Enter the marks: "))

if 90 <= marks <= 100:
    print("Grade A")
elif 75 <= marks <= 89:
    print("Grade B")
elif 60 <= marks <= 74:
    print("Grade C")
elif 40 <= marks <= 59:
    print("Grade D")
elif 0 <= marks < 40:
    print("Fail")
else:
    print("Invalid marks")
