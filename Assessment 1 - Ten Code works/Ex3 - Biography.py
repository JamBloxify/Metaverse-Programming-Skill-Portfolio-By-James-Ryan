thisdict = {"Name:": input("What is your first and second name? "),
            "Hometown:": input("Where were you born? "),
            "Age:": input("How old are you? ")
    }
# A dictionary is created to store user-inputted values in the keys.

for x, y in thisdict.items():
  print(x, y) 

""" x is the new variable made, which stores and collects the dictionary's items inside.
When printing x, it will display each item, as tuples in a list """