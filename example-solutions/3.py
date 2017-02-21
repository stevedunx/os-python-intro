#
# PART ONE
#

# Create an array
a = [1, 29, 26, 26, 23, 21, 18, 16, 13, 10, 8, 5, 3, 26]

# There is an error in the list
a.pop() # remove the last element
a.append(31) # append the new value

# How many items are there in the list
len(a)

# Retrieve every other value from the list
a[::2]

# Sort the list so that it starts with 31 and ends with 1.
a.sort(reverse=True)  # or a.sort(); a.reverse()

# Create another variable that is a set of the unique values from the list
b = set(a)

# What is wrong with a[len(a)]? The first element must be an index, which starts from 0, whereas a length starts from 1. Hence, it should be:
a[len(a) - 1]
# or
a[-1]

# How do you make a backwards slice work?
a[-1::-1]
# or
a[::-1]

#
# PART TWO
#

# Create a dictionary the Middle as keys and YOB as the values
c = {'Arthur': 1941,
     'Marwood': 1939,
     'Vance': 1940,
     'Graham': 1942,
     'Edward': 1943}

# Add 'Bone' to the dictionary, with a value of 1943
c['Bone'] = 1943
c['Graham']

# What is wrong with d[2]? There is no key called 2. Probably what is meant is:
d = {1: 4, 5: 7, 24: 9}
d[24]

