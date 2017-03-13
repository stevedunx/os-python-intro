# PART ONE

x = 9
y = 15.0

10 + 100  # returns 110
10 - 90   # returns -80
x * y     # returns 135.0
x ** 2    # returns x^2, 81
0.1 * 3   # returns 0.30000000000000004 - this is because of floating point representation - be careful
9.0 / 30  # returns 0.3 - so 0.3 can be represented cleanly!
# The following two have different results in Python 2 and 3. Python 3 does not do integer maths.
2 / 5     # mathimatically, should be 0.4 (and is result in Py3); but Py2 returns 0, this is because Python sees two integers and is doing integer maths
x / 5     # mathimatically, should be 1.8 (and is result in Py3); but Py2 returns 1, which shows that integer maths actually truncates the decimal rather than rounding
y / x     # returns 1.6666666666666667, because Python has spotted a floating point number and is therefore doing floating point maths
"1" + "2" # returns '12', because the two values are strings, so Python believes that you mean concatenate these strings together
"0" * 2   # returns '00', because Python believes that you have asked for the string to be repeated 2 times.

m = 12
m += 1
# m is now 13; it is the equivalent of m = m + 1

n = 12
n -= 2
# n is now 10; it is the equivalent of n = n - 2

# PART TWO

x = "3"
y = 4

# To add the numbers together
print(int(x) + y)

# To concatenate the strings together
print(x + str(y))

# Or you could do...
# print("{0}{1}".format(x, y))
