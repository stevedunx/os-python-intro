# Lists

Lists are ordered collections of items. They can have anything in them and can be mixed. Normally they only have one type in them.

```
a_list = [4,7,9,6]
a_mess = ['string',14,54.3]
```

Parts of the list can be extracted, see [worksheet](3-list-worksheet.md).

Other information can be obtained from the list:

* `len(a_list)` will get the length of the list.

Once a list is created, it can be changed:

* `a_list[2] = 'updated value'` will change the value of element at position 2 in `a_list`.
* `a_list.append('new value')` will add a `'new value'` end of `a_list`.
* `a_list.pop()` will remove the last element of `a_list`. 
* `a_list.sort()` will sort `a_list`.

# Tuples

Tuples are like lists, but cannot be changed. Tuples can be faster than lists.

* `a_tuple = (1,3,5,7,9)` will create a new tuple

Data can be obtained from a tuple just like lists, but nothing can be added to an existing tuple.

# Sets

Sets are unordered collections that have a unique set of values.

* `a_set = {1,2,3,4,5}` will create a set with defined values
* `a_set = set()` will create an empty set

# Dictionaries

Dictionaries are an unordered collection of items, whose values are accessed via keys.

* `a_dict = {1:4, 5:7, 24:9}` will create a dictionary with numbers as keys
* `python_dict = {'Arthur':1941,'Marwood':1939}` will create a dictionary with strings as keys

Other information can be obtained from the dictionary:

* `python_dict.keys()` will list the keys in the dictionary.

A part of the dictionary can be extracted by key:

* `python_dict['Marwood']`

Once a dictionary is created, it can be changed:

* `python_dict['Vance'] = 1940` will add another entry at key `Vance` with the value `1940`.

# It can get complex... 

The values in a list or dictionary can be other lists or dictionaries.

The following is an example of GeoJSON, but is also valid Python syntax:

```
feature_collection = {
    "type": "FeatureCollection",
    "features": [
        {
            "type": "Feature",
            "geometry": {
                "type": "Polygon",
                "coordinates": [[[-1.47, 50.94], [-1.47, 50.93], [-1.46, 50.93], [-1.47, 50.94]]]
            }
        },
        {
            "type": "Feature",
            "geometry": {
                "type": "LineString",
                "coordinates": [[-1.47, 50.94], [-1.46, 50.94], [-1.46, 50.93]]
            }
        }
    ]
}
feature_collection["features"][1]["geometry"]["coordinates"][1][0] # get the X coordinate of the second vertex of the geometry of the second feature
```
