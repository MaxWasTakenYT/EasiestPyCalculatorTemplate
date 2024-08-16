# the Easiest Python Calculator Template (EPCT Version 1.3)
# Created by jstmax! (@MaxWasTakenYT on github, bit.ly/mx_info for more information on me)
# License info: The Unlicense, for more informations visit: <https://unlicense.org>

# Here we go!
# So first things first:
# Importing modules
# To make things easy, we are only going to use 'time'
# Which we will use to set how much time passes from a text to another
# With other modules like 'os', you can even clear the text thats on screen
# But we do not care about complex stuff, ONLY. EASY (and beauty). STUFF.
# Because doing otherwise would make me a liar about calling this:
# "the Easiest Python Calculator Template", notice anything? yes: EASIEST
# Apart from this stupid stuff, let's continue!
# By importing 'time' into the pwogwam
import time

# here i make gonna make a function that we don't need (for now), but i will get back to this later, just get past this part and dont worry about it (for now) :)
def dbyz():
  from tkinter import messagebox as tkmsg
  def db0err():
    tkmsg.showerror(title="Why do you this to me?", message="You are an awful person, why are you so cruel to do this to me?")

  if logoper == '/' and num2 == 0:
    db0err()
  else:
    pass

# We are back.
# Here we greet the user and let him know what we are doing with this application, using the 'print()' function.
print("Welcome to the Easiest Python Calculator")

# with 'time.sleep(number of seconds to wait)'
# we will make text disappear to make this app less "dogsh!t"
time.sleep(1)
print("With no libraries and no complicated stuff")
time.sleep(1)
print("I'm going to try and make it a replit template too")
time.sleep(1.5)
print("Let's go")

# If you didn't know (or didnt understand it..), putting '#' at the beginning of a line will make it so that every content that is written in that line, will become a comment.

# Now we get the numbers we need to calculate from the user (plus the logopererator)
# Using the input() function, inside of a float() function, which in itself is inside of a new value (num1), we can get input from the user, just like this:

# Note: Do not make the mistake of using both print() and input()
# Basically:
# This is a big nono: 'valuename = input(print("Question? "))'
# It will return 'None' and just will just be ugly as f*ck
# This on the other hand, is a big yes yes and will work with no issues: 'valuename = input("Question? ")'
time.sleep(0.8)
num1 = float(input("Enter the first number: "))
# As you can see, we put a space after the question, this will make it cleaner for the user:
# He's not going to see "Enter the first number:|"
# But instead he's going to see "Enter the first number: |"
# (Just so you can get the idea: '|' represents the text cursor)

# Now let's get the logical logopererator in the same fashion :)
time.sleep(1)
logoper = input("Enter the logical logopererator ('+', '-', '*' or '/'): ")

# And finally we get the last value (the second number)
time.sleep(1)
num2 = float(input("Enter the second number: "))

# And now the most """complicated""" thing yet, but don't worry, it's going to be explained perfectly (or at least i'll try my best!)
# Let's calculate stuff!

# TL;DR: we are going to use an 'if' function to check what logopererator the user chose and do the math based on that.
if logoper == '+': # Case #1 "Addition"
  res = num1 + num2
  print(res)
elif logoper == '-': # Case #2 "Subtraction"
  res = num1 - num2
  print(res)
elif logoper == '*': # Case #3 "Multiplication"
  res = num1 * num2
  print(res)
elif logoper == '/': # Case #4 "Division"
  dbyz()
  res = num1 / num2
  print(res)
  
# And we are done! Our RLY-EZ calculator is finished!
# I know this is a VERY simple calculator, but remember, this is:
# "the EASIEST Python Calculator Template"
# If you want to experiment with simple Python code (as a newbie) you can edit this code and do whatever you want with it
# According to <https://unlicense.org>


# just a small thing, before ending this..
# well.. for fun's sake, i made a "divided by zero" error!!
# and yes, it was that thing i told you not to care about in the beginning (lines #18-27)
# IMPORTANT NOTE: this error thing, is a bit more complex for beginners (since it uses tkinter), do not actually try and make this if you just started
# this was just for fun.



# Now we are actually done, thanks for reading/trying/doing anything,
# -... .. - .-.-.- .-.. -.-- -.-.-- -- -..- .. -...-. --- @ jstmax! // bit.ly/mx_info
