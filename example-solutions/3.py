# Create an array
a = [1, 29, 26, 26, 23, 21, 18, 16, 13, 10, 8, 5, 3]

# Append the value 31 to the end of the list
a.append(31)

# Sort the list so that it starts with 31 and ends with 1.
a.sort(reverse=True)  # or a.sort(); a.reverse()

# Create another variable that is a set of the unique values from the list
b = set(a)

# Create a dictionary the Middle as keys and YOB as the values
c = {'Arthur': 1941,
     'Marwood': 1939,
     'Vance': 1940,
     'Graham': 1942,
     'Edward': 1943}
c['Marwood']
c['Bone'] = 1943