# A closure in Python is a function that remembers the values of variables from its enclosing scope, even after the enclosing function has finished executing.

# How closures work:-

# A closure is created when:

# A function is defined inside another function.
# The inner function refers to variables from the outer function.
# The outer function returns the inner function.

# eg:

def outer(message):
    def inner():
        print(message)
    return inner

greet = outer("Hello")
greet()


# Even though outer() has already returned, inner() still remembers the value of message.
# Normally, local variables disappear when a function finishes. However, if an inner function needs them, Python keeps those variables alive as part of the closure.

def multiplier(x):
    def multiply(y):
        return x * y
    return multiply

times3 = multiplier(3)
times5 = multiplier(5)

print(times3(10))  # 30
print(times5(10))  # 50



# Code                 What happens?
# inner()              Function runs immediately
# return inner         Inner function is returned and remembers message
# return inner()       Runs inner and returns its result – not a closure
# greet = outer("Hello")  Closure is being used
# greet()

