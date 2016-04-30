print "How old are you?",
# raw_input is like prompt(), and below the user input is getting stored in variables age, height, and weight
age = raw_input()
print "How tall are you?",
height = raw_input() 
print "How much do you weigh?",
weight = raw_input() 

print "So, you're %r old, %r tall and %r heavy." % (age, height, weight)