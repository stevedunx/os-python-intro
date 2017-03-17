# Step 1

a_list_of_films = [
    "And Now for Something Completely Different",
    "The Holy Grail",
    "Life of Brian",
    "The Meaning of Life"
]
for film in a_list_of_films:
    print("{name} has a length of {length}".format(name=film, length=len(film)))

# Step 2

i = 1
while i <= 10:
    print "{num} multiplied by 10 is {result}".format(num=i, result=i*10)
    i += 1

# Bonus

some_fib = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
print ([x for x in some_fib if (x % 2 == 0 or x % 5 == 0)])

