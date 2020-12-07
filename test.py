# Create the logging_decorator() function 👇
def logging_decorator(func):
    def wrapper(*args):
        sum = 0
        values = ''

        for arg in args:
            sum = sum + int(arg)
            values = str(arg) + ", " + values

        print("You call a " + func.__name__ + "(" + values[0:-2] + ")")
        print('It return: ' + str(sum))
        return sum

    return wrapper


# Use the decorator 👇
@logging_decorator
def a_function(*args):
    print()


a_function(1, 3, 5)
