# *** NOTE**** actual decorators are at the bottom! ALl these above ARE PRE EXAMPLES TO GET YOU PREPARED FOR DECORATORS!

# EXAMPLE 1

# s = "GLOGBAL VARIABLE!"

# def func():
#     mylocal = 10
#     print(locals())
#     # calling this as a dictionary find the key value pair of s
#     print(globals()["s"])

# func()

# EXAMPLE 2
# def hello(name="ryan"):
#     return "hello " + name

# print(hello())

# # setting equal to the function itself:
# mynewgreet = hello

# print(mynewgreet())


# Example 3:
# Becuase of scope, greet function and welcome function cannot be called from outside of hello()
# def hello(name="ryan"):
#     print("the hello() function has been run!")

#     def greet():
#         return "this string is inside  greet() function"
#     def welcome():
#         return"this string is inside wlecome() function"
#     print(greet())
#     print(welcome())
#     print("end of hello() function")

# hello()

# example 4: Returning a function:
# def hello(name="ryan"):
#     print("the hello() function has been run!")

#     def greet():
#         return "this string is inside  greet() function"
#     def welcome():
#         return"this string is inside wlecome() function"

#     if name == "ryan":
#         return greet 
#     else: 
#         return welcome

# # setting x to what ever the result is of hello()
# x= hello()
# print(x())
# # same as:
# print(hello())


# Example 4: pasing in a function as an agument:
# def hello():
#     return "Hi Ryan!"

# def other(func):
#     print("hello")
#     print(func)

# # passing in function as a paramater to another function - running a function from within a function!
# other(hello)


# # DECORATORS!:
# def new_decorator(func):
    
#     def warp_func():
#         print("Code hgere befoire executing func")
#         func()
#         print("func() has been called")

#     retun warp_func

# defining a new function while setting its results to a function within another function!:
# func_needs_decorator = new_decorator(func_needs_decorator)

# # calling the newly declared function:
# func_needs_decorator()

# **THIS CAN ALSO BE DONE UTILIZING THE "@" SYMBOL!**:
# Example:
# DECORATORS!:
def new_decorator(func):
    
    def warp_func():
        print("Code here befoire executing func")
        func()
        print("func() has been called")

    return warp_func

# same thing as doing this:    func_needs_decorator = new_decorator(func_needs_decorator):
@new_decorator

def func_needs_decorator():
    print("This function is in need of a decorator!")

func_needs_decorator()





