# setting format of the output
formatter = "{} {} {} {}"
# provide input
print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format (True, False, False, True))

#repeat formatter elements
print(formatter.format(formatter, formatter, formatter, formatter))

# type your own input
print(formatter.format (
    "accountable for actions",
    "not for intentions",
    "sorry for the inconvenience",
    "we are trying to change the world"
))