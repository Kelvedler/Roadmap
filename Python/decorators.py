def new_decorator(function):

    def wrap_func():
        print('Code here before executing func')
        function()
        print('function() has been called')

    return wrap_func


@new_decorator
def func_needs_decorator():
    print('This function needs decorator!')


# func_needs_decorator = new_decorator(func_needs_decorator)


func_needs_decorator()