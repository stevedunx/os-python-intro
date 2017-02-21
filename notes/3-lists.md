# Lists

Lists are ordered collections of items. They can have anything in them and can be mixed. Normally they only have one type in them.

```
a_list = [4,7,9,6]
a_mess = ['string',14,54.3]
```

Parts of the list can be extracted:

`a_list[0]` will get the first element of the list.
`a_list[-1]` will get the last element of the list.
`a_list[0:2]` will get a list of elements, from index 0 up to, but not including, 2.
`a_list[1:]` will get a list of elements, from index 1 up to the end of the list.
`a_list[:-1]` will get a list of elements, from the beginning up to, but not including, the last value in the list.
`a_list[::2]` will get every other element from the list, from start to end.

Other information can be obtained from the list:

`len(a_list)` will get the length of the list.

Once a list is created, it can be changed:

`a_list[2] = 'updated value'` will change the value of element at position 2 in `a_list`.
`a_list.append('new value')` will add a `'new value'` end of `a_list`.
`a_list.pop()` will remove the last element of `a_list`. 
`a_list.sort()` will sort `a_list`.

# Tuples

Tuples are like lists, but cannot be changed. Tuples can be faster than lists.

`a_tuple = (1,3,5,7,9)`

# Dictionaries

## Dictionaries are an unordered collection of items, whose values are accessed via keys.

`a_dict = {1:4, 5:7, 24:9}` will create a dictionary with numbers as keys
`python_dict = {'Arthur':1941,'Marwood':1939}` will create a dictionary with strings as keys

A part of the dictionary can be extracted by key:

`python_dict['Marwood']`

Once a dictionary is created, it can be changed:

`python_dict['Vance'] = 1940` will add another entry at key `Vance` with the value `1940`.

# It can get complex... 

The values in a list or dictionary can be other lists or dictionaries.