x = 1000
# this creates an int object with 1000 and x is a variable that points to that object
x = 500
# this creates a new object with 500 and x is redirected to it, and later object 1000 is collected
y = x
# this just assigned y to point to the object 500, but nothing else

print(id(x))
print(id(x)==id(y))
# the id can be used to show the memory address to which the variable is pointing to,
# but it is only used in python tutorials, not in production

print(x is y)
print(x is None)

# vairables are not boxes holding a value, in python these are named references to objects

p = [1,2,3]
q = [1,2,3]
print(p==q) # value equality true
print(p is q) # reference equality false

# value equaility == can be overriden by the developer

def extend_and_print(k):
    k.append(48)
    print("k=", k)

m = [4,5,6]
extend_and_print(m) # the original m is changed
print("m=", m)

# this happens because function arguments are tranferred pass-by-object-reference 
# => the objects themselves are not copied

#default function arguments
def banner(message, border='-'):
    print(border * len(message))
    print(message)
    print(border * len(message))

banner("Hi there")

# there is a pitfall, because default arguments are evaluated when def is executed , and it is evaluated only once
# with immutable default values, there is no problem
def add_spam(meals = []):
    meals.append('spam')
    print(meals)

add_spam()
add_spam()
add_spam()

#fix:
def smart_add_spam(meals = None):
    if meals == None:
        meals = []
    meals.append('spam')
    print(meals)

smart_add_spam()
smart_add_spam()
smart_add_spam()
