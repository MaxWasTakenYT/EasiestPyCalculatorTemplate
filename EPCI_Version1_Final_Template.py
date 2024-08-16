# the Easiest Python Calculator Template (EPCT Version 1)
# Created by jstmax! (@MaxWasTakenYT on github)
# License info: The Unlicense, for more informations visit: <https://unlicense.org>

# Here we go!
# So first things first:
# Importing modules
# To make things easy, we are only going to use 'time'
# Which we will use to set how much time passes from a text to another
# Obviously with other modules like 'os', you can even clear the text that's on screen
# But we do not care about complex stuff, ONLY. EASY. STUFF.
# Because doing otherwise would make me a liar about calling this:
# "the Easiest Python Calculator Template", notice anything? yes: EASIEST
# Apart from this stupid stuff, let's continue!
# By importing 'time' into the "thing"
import time

# now im gonna make a function that we dont need for now, but i will get back to this later, just get past this part and dont worry about it for now :)
def dbyz():
  from tkinter import messagebox as tkmsg
  def db0err():
    tkmsg.showerror(title="Why do you this to me?", message="You are an awful person, why are you so cruel to do this to me?")

  if op == '/' and no2 == 0:
    db0err()
  else:
    pass

# We are back.
# Here we welcome the user and let him know what we are doing with this application.

print("Welcome to the Easiest Python Calculator")

# with time.sleep(number of seconds to wait)
# we will time text to make this app less "horsesh!t"
time.sleep(1)
print("With no libraries and no complicated stuff")
time.sleep(1)
print("I'm going to try and make it a replit template too")
time.sleep(1.5)
print("Let's go")

# If you didn't know (or didnt understand it..), putting '#' at the beginning of a line will make it so that every content that is written in that line, will become a comment.

# Now we get the numbers we need to calculate from the user (plus the operator)
# Using the input() function, inside of a float() function, which in itself is inside of a new value (no1), we can get input from the user, just like this:
# Note: Do not make the mistake of using both print() and input()
# Basically:
# This is a big nono: valuename = input(print("Question? "))
# It will return None and just be ugly as f*ck
# This is a big yesyes: valuename = input("Question? ")
# This will work just fine
time.sleep(0.8)
no1 = float(input("Enter the first number: "))
# As you can see, we have put a space after the question, so it makes it better for the user:
# He's not going to see "Enter the first number:|"
# But instead he's going to see "Enter the first number: |"
# (In which '|' is the text cursor, to get the idea)

# Now let's get the operator for the math operation in the same style :)
time.sleep(1)
op = input("Enter the operator ('+', '-', '*' and '/'): ")

# And finally (for the user) we get the last value, the second number
time.sleep(1)
no2 = float(input("Enter the second number: "))

# And now the most complicated thing yet, but don't worry, it's going to be explained perfectly (Or at least i hope you'll understand)
# Let's calculate stuff!

# To make this easy and fast, we are going to use an 'if' function to check what operator the user gave us,
# And calculate the operation based on that.
if op == '+':
  res = no1 + no2
  print(res)
elif op == '-':
  res = no1 - no2
  print(res)
elif op == '*':
  res = no1 * no2
  print(res)
elif op == '/':
  dbyz()
  res = no1 / no2
  print(res)
# And we are done, our EZ calculator is 100% done!
# I know this is very simple of a calculator, but remember this is:
# "the EASIEST Python Calculator Template"
# If you want to experiment with python (possibly being a new one to coding) you can edit this code and do whatever you want with it
# According to <https://unlicense.org>


# just a small thing, before ending..
# well.. for fun's sake, i made a "divided by zero" error!!
# and yes, it was that thing i told you not to care about before
# IMPORTANT NOTE: this was  a lot more complex for beginners so, do not actually try and make this if you just started, this was just for fun.


# Now we are truly done, thanks for reading/trying/doing anything,
# max, out :)
