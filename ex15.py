from sys import argv 

#gives the name of this file and the name of the text file to argv
script, filename = argv

#the open fn takes the filename (ex15_sample.txt) as an argument, and stores the result of that function call in a variable, txt. the result of the open function call is a file object. 
txt = open(filename)

#print the message concatenated with the filename
print "Here's your file %r:" % filename
#call the read method on the file object, which is stored in the txt variable. this will read the file, printing out the contents
print txt.read()

print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()

#or shorter and not stored in a variable:
# print open(raw_input("> ")).read()
