# Unpacking arguments "*"
print(1, 2, 3, 4, 5)

numbers = [1, 2, 3, 4, 5]
print(numbers)

# Unpack list before printing
# 5 mini arguments
print(*numbers)

# Unpack string
print("abc")
print(*"abc")
# same as printing each letter individually


# Packing arguments
# Limited way
def add(x, y):
    return x + y


add(10, 10)


# More efficient
def add(*numbers):
    total = 0
    for number in numbers:
        total = total + number
    return(total)


print(add(1, 2, 3, 4, 5, 6, 7))

# Unpacking keyword arguments **

def about(name, age, likes):
    sentence = "Meet {}! They are {} years old and they enjoy {}".format(name, age, likes)


dictionary = {"name": "Keenan", "age": 21, "likes": "Women"}

print(about(**dictionary))


# Packing keyword stats
def foo(**kwargs):
    for key, value in kwargs.items():
        print("{}:{}",format(key, value))


foo(Ambre= "male", Keenan= "female", Kayla= "Unknown")