import time
# ^ For the delay function
ans = "12345"
# ^ The answer to the question.
a = ""
# ^ A variable with a blank value, used for user input.
count = 0
# ^ Count ammount at the start, and will increase by one.
ving = "Verifying..."
# ^ Aesthetic
vfied = "The password matches."
# ^ The password is verified and matches.
nfied = "The password does not match."
# ^ The password is verified and does NOT match.
win = "You are now logged in."
# ^ Displayed when the user successfully inputs the correct password
fail = "You have failed to input the correct password, the authorities have been informed."
# ^ Displays after the user fails to input the right password after 5 attempts.
start = "Welcome, User, please enter your password. You have 5 attempts left."
# ^ The intro before the question, also displays the attempts.
four = "You have 4 attempts left"
three = "You have 3 attempts left"
two = "You have 2 attempts left"
one = "You have 1 attempt left"
# ^ The four variables above is displayed to remind the user how many chances left.

print(start)
# ^ Prints the intro

time.sleep(3)
# ^ Delays the code.

while a != ans:
    if count == 1:
        print(ving)
        time.sleep(3)
        print(nfied)
        time.sleep(1)
        print(four)
        
    if count == 2:
        print(ving)
        time.sleep(3)
        print(nfied)
        time.sleep(1)
        print(three)
        
    if count == 3:
        print(ving)
        time.sleep(3)
        print(nfied)
        time.sleep(1)
        print(two)  
        
    if count == 4:
        print(ving)
        time.sleep(3)
        print(nfied)
        time.sleep(1)
        print(one)    
        
    if count == 5:
        print(ving)
        time.sleep(3)
        print(nfied)
        break
    
    else:
        a = input("Enter your password: ")
        count += 1
        if a.isalpha():
            print("Integers only.")
        """ ^ Checks if the input is using alphabets, and if it is, 
            it will give feedback and increase count."""
      
    
""" ^ While function loops while a is not equal to the answer.
If function runs when the count number matches. Every wrong answer displays the incorrect message and chances left.
Else prints the question for the user to input, and increases the count by 1.
At count 5, if the user gets the answer wrong, the code will break."""

if a == ans:
    print(ving)
    time.sleep(3)
    print(vfied)
    time.sleep(1)
    print(win)
    
else:
    time.sleep(1)
    print(fail)
    
""" ^ In this if else function, if a is equal to the answer, it will print feedback saying
user is correct and log in.
If not, it will print the fail message and inform the authorities."""