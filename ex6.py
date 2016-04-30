x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s" % (binary, do_not)

print x
print y

#%r and %s are similar, but %r and repr are designed to be unambiguous (it's a string? quotation marks), where as %s and str are designed to be human readable. http://stackoverflow.com/questions/1436703/difference-between-str-and-repr-in-python
print "I said: %r." % x
print "I also said: '%s'." % y

hilarious = False
#joke_evaluation anticipates a string to be inserted
joke_evaluation = "Isn't that joke so funny?! %r"

#inserting variable hilarious into string joke_evaluation
print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

#string concatenation
print w + e