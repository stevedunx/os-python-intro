# Loops

## for

A for loop goes through an iterable, like a list, and allows you to perform something for each item.

```
a_list = range(0,10)
for an_item in a_list:
    print("an_item has a value of " + an_item)
```

Note the Python syntax of a colon and then strict indentation for blocks of code.

Strings have methods that allow you to change the string. You can call these methods in a loop.

```
a_list_of_films = [
    "And Now for Something Completely Different",
    "The Holy Grail",
    "Life of Brian",
    "The Meaning of Life"
]
for film in a_list_of_films:
    print("In uppercase, the film's name is " + film.upper())
```

## while

A while loop allows you to perform something until the while condition becomes false. In the example below, up to and including when `i` is 10.

```
i = 0
while i <= 10:
    print("The current number is " + str(i))
    i = i + 1
```

Conditions are covered more in section 6.