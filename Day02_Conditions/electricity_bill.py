units = int(input("Enter units consumed: "))

if units < 0:
    print("Invalid units")

elif 0 <= units <= 100:
    bill = units * 5
    print("Your electricity bill is:", bill)

elif 101 <= units <= 200:
    bill = units * 7
    print("Your electricity bill is:", bill)

else:
    bill = units * 10
    print("Your electricity bill is:", bill)
