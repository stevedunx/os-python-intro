# Part 1

item_stock = 1
order_quantity = 1
buyer_wants_delivery = True
maximum_delivery_distance = 250
buyers_distance_from_shop = 208

# restock required
if order_quantity == item_stock: print "restock required"

# enough in stock
if order_quantity <= item_stock: print "enough"

# buyer wants delivery and is within delivery distance
if buyer_wants_delivery and buyers_distance_from_shop <= maximum_delivery_distance:
    print "within"

# Part 2

# the indentation is a mixture of tabs and spaces.
# Tabs can be interpreted as differing number of spaces depending on the situation.
# GitHub and Python interpret them as 8 spaces; NotePad++ and the console interpret them as 4.
# It is better to use only spaces.
if True:
    print "This is true"
    print "But it might not be the truth"
