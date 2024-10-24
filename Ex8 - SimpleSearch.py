thelist = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]
a = input("Input name to check if it's in the list: ")
# ^ A list followed by a variable containing input for the user to type down.

if a in thelist:
    print("This name exists.")
else:
    print("This name doesn't exist (Be case-sensitive)")
# ^ This checks if the input from the user exists in the list, and will provide feedback.

