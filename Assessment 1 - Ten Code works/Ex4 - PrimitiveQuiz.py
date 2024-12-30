intro = """Primitive Quiz!
The question requires a CASE-SENSITIVE answer
Good Luck!"""
# ^ The intro before the question is displayed
a = "Two chances left"
b = "One chance left"
# ^ The two variables display how much chances are left when printed.
c = "You lose. The answer is Paris."
# ^ This variable will be printed if the user doesn't answer correctly.
ans = "Paris"
# ^ This is the answer for the question
right = "Correct, well done!"
# ^ Printed when the user answers correctly.
wrong = "Incorrect." 
# ^ Tells the user their answer is wrong.
q = ""
# ^ A variable with a blank value inside, this is for the user input.
count = 0
# ^ The counts at the start, each wrong answer increases it by one
import time
# ^ This is just for the delay function.

print(intro.strip())
# ^ Prints the intro function, strip removes any blank space before and after the sentence.     

time.sleep(2)
# ^ Delay before question is printed

while q != ans:
    if count == 1:
        print(wrong)
        print(a)
        
    if count == 2: 
        print(wrong)  
        print(b)   
            
    if count == 3:
        break

    else:
        q = input("What is the capital of France? ")
        count += 1
"""while q is not equal to the answer, the count will increase by 1 while displaying the question.
If the answer is wrong, it will print the wrong and chances variable to tell the user they're wrong, and how many chances left.
At the last count, if the user gets it wrong, the code will break."""

if q == ans:
    print(right) 
else:
    print(c)
"""This if function will run when the user inputs the right answer, otherwise, once the code above breaks at the third count, it will print the losing statement."""


    