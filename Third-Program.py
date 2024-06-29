#Third Python Program
##Created to UMGC DATA 620 by Dr. George Cross
##List:
##A list is the Python equivalent of an array
##
empList=[] # empty list
print(empList)
xs = [3, 1, 2] # Create a list
print(xs, xs[2]) # Prints "[3, 1, 2] 2"
print(xs[-1]) # Negative indices count from the end of the list; prints "2"
xs[2] = 'George' # Lists can contain elements of different types
print(xs)# Prints "[3, 1, 'George']"
#Some functions to the List:
xs.append('bar') # Add a new element to the end of the list
print(xs) # Prints "[3, 1, 'George', 'bar']"
x = xs.pop() # Remove and return the last element of the list
print(x, xs) # Prints "bar [3, 1, 'George']"
print() # blank
print(xs)
print() # blank
#Loops: You can loop over the elements of a list like this:
animals = ['cat', 'dog', 'monkey']
for animal in animals:
    print(animal)
#tab is important
# Prints "cat", "dog", "monkey", each on its own line
print(animals) # print the list again
print() # blank
#Another List with Float values
sales = [500.44,400.29,300.22,200]
for ss in sales:
    print(ss)
#Another List with Variables values
R100="R100"
R99="R99"
R60="R60"
RegionCodes = [R100,R99,R60]
for rc in RegionCodes:
    print(rc)
#Dictionaries
#A dictionary stores (key, value) pairs
print() # blank
d = {'cat': 'cute', 'dog': 'furry'} # Create a new dictionary with some data
print(d) #print the dictionary
print() # blank
print(d['cat']) # Get an entry from a dictionary; prints "cute"
print('cat' in d) # Check if a dictionary has a given key; prints "True"
print('car' in d) # Check if a dictionary has a given key; prints "False

d['fish'] = 'wet' # Set an entry in a dictionary
print(d['fish']) # Prints "wet"
print(d) #print the dictionary again after appending with fish
print() # blank
#Loops: It is easy to iterate over the keys in a dictionary
d = {'person': 2, 'cat': 4, 'spider': 8}
for animal in d:
    legs = d[animal]
print('A %s has %d legs' % (animal, legs))
print('A {0:s} has {1:d} legs'.format(animal, legs))
# Prints "A person has 2 legs", "A cat has 4 legs", "A spider has 8 legs"