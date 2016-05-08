i = 0 
numbers = []

while i < 6:
    print "At the top i is %d" % i 
    numbers.append(i)

    i = i + 1
    print "Numbers now: ", numbers
    print "At the bottom i is %d" % i 

print "The numbers: "
for num in numbers: 
    print num

print "Now as a for-loop:"

numbers_2 = range(0, 6)
for num_2 in numbers_2:
    print num_2