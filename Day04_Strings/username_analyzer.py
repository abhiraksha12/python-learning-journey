username = input("Enter your name: ")

print("Uppercase:", username.upper())
print("Length:", len(username))
print("Reversed:", username[::-1])

if username.startswith("A"):
    print("Starts with A")
else:
    print("Does not start with A")
