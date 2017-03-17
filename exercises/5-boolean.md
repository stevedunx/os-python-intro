# Boolean

A Norwegian Blue is being sold in a shop in Ipswich. The shop has 1 in stock. The shop does deliveries within 250 miles.

A buyer wishes to order a Norwegian Blue. The buyer wants it delivered, and lives 208 miles away in Bolton.

Using the following variables:

```
item_stock = 1
order_quantity = 1
buyer_wants_delivery = True
maximum_delivery_distance = 250
buyers_distance_from_shop = 208
```

Write a separate if statements to check:
* whether the `order_quantity` matches the `item_stock`, then print "restock required"
* whether the `order_quantity` is less than or equal to the `item_stock`, then print "enough" otherwise print "out of stock"
* whether the `buyer_wants_delivery` and the `buyers_distance_from_shop` is less than the `maximum_delivery_distance`, then print "within"

# Indentation

What is wrong with the following statement?

```
if True:
    print "This is true"
	print "But it might not be the truth"
```

[< Previous](4-maths.md) | [Outline](../CourseOutline.md) | [S](../example-solutions/5-boolean.py) | [Next >](6-loops.md)