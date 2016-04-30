#import the argv module from sys module 
#argv is "argument variable"
from sys import argv
script, first, second, third = argv

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third

fourth = raw_input('Next var? ')
print "fourth arg is:", fourth