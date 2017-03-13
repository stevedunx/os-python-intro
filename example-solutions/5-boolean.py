# Part 1

item_stock = 1
order_quantity = 1
buyer_wants_delivery = True
maximum_delivery_distance = 250
buyers_distance_from_shop = 208

# restock required
if order_quantity == item_stock:
    print "restock required"

# enough in stock
if order_quantity <= item_stock:
    print "enough"

# buyer wants delivery and is within delivery distance
if buyer_wants_delivery and buyers_distance_from_shop <= maximum_delivery_distance:
    print "within"

# Part 2

some_fib = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
print ([x for x in some_fib if (x % 2 == 0 or x % 5 == 0)])


# Bonus

def fizzbuzz(n):
    for i in range(1, n + 1):
        if i % 15 == 0:
            print("fizzbuzz")
        elif i % 3 == 0:
            print("fizz")
        elif i % 5 == 0:
            print("buzz")
        else:
            print(i)

fizzbuzz(16)