# Step 1

a_list_of_films = [
    "And Now for Something Completely Different",
    "The Holy Grail",
    "Life of Brian",
    "The Meaning of Life"
]
for film in a_list_of_films:
    print(film + " has a length of " + str(len(film)))

# Step 2



# Bonus
second_last_number = 0
last_number = 1
while last_number < 34:
     new_number = second_last_number + last_number
     print new_number
     # prepare for next iteration, shift variables
     second_last_number = last_number
     last_number = new_number