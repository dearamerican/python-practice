from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL_C (^C)."
print "If you go want that, hit RETURN."

raw_input("?")

print "Opening the file..."
#The open function defaults to read status; it tries to be safe by forcing you to explicitly state that you want to write to the file--you do that by giving it the string of "w". You don't need to pass "r" to be in read-only mode, but you can if you want. 
#"a" is the arg to pass instead of "w" if you want to add or append something to the file without deleting all the contents first
target = open(filename, 'w')

print "Truncating the file. Goodbye!"
#optional truncate command in write mode - it deletes everything automatically unless you specify a file size to truncate it to by passing a number as arg to truncate
target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

#too long: 
# target.write(line1)
# target.write("\n")
# target.write(line2)
# target.write('\n')
# target.write(line3)
# target.write("\n")

#better:
target.write("\n" + line1 + "\n" + line2 + "\n" + line3)

print "And finally, we close it."
target.close()
target = open(filename)
print target.read()
