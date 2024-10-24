yes = "y"
no = "n"
caldict = {
     1:"January, 31 days",
     2:"February, 28 days",
     3:"March, 31 days",
     4:"April, 30 days",
     5:"May, 31 days",
     6:"June, 30 days",
     7:"July, 31 days",
     8:"August, 31 days",
     9:"September, 30 days",
     10:"October, 31 days",
     11:"November, 30 days",
     12:"December, 31 days"
     }
# A dictionary is created, storing numbers as keys, representing each month.
# The values stored inside the keys are the amount of days in that month.
month = int(input("Which month would you like to know the number of days? (1-12): "))
# ^ Variable created that asks the user to input a month, STRICTLY, in number form, as shown with the integer function before the input.
error = "That number does not correspond to any of the 12 months."
# ^ This message will display when the user inputs a number that isn't within the range of 1 - 12.
if month > 12: # If number is above 12, it'll prompt an error message.
    print(error)
elif month == 2: # Checks if the user inputs February, executing another code.
        Year = int(input("What year is it? ")) # Asks a string input
        if (Year % 4 == 0):  # If yes, it'll provide the number of days for leap year.
            print("February (Leap Year), 29 days")
        else: # If no, it'll provide the number of days without leap year.
            print(caldict[month])
else:
    print(caldict[month])
    
""" ^ This if else function runs when user inputs a number above 12.
If the number is below 12, it will print the dictionary's value based on the user input."""

