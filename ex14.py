from sys import argv

script, user_name, age = argv
prompt = 'Type your answer: '

print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me, %s?" % user_name
likes = raw_input(prompt)

print "Where do you live, %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?" 
computer = raw_input(prompt)

print """
Alright, %s, so you're %r years old, and said %r about liking me. You live in %r. Not sure where that is. And you have a %r computer. Nice.
""" % (user_name, age, likes, lives, computer)