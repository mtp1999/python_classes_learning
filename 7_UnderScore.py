"""
This section is about underscore usages in python.
"""


# use _ for ignoring
tuple1 = (1, 2, 3)
a, _, b = tuple1
print(a, b)

tuple2 = (1, 2, 3, 4, 5, 6)
a, b, *_, c = tuple2
print(a, b, c)


# using in loop without using a variable
for _ in range(10):
    print(_)

# using as a variable when it doesnt important what the name of the variable is.
_ = 5
while _ < 8:
    print(_, end=' ')
    _ = _ + 1

"""
_var and _func() are protected variables and functions 
and cannot import and use in other python files
(but we can use them with PythonFile._var in other python files)
"""
_var = 'protected variable'


def _func():
    print('protected function')


"""
we use var_ when we want to name a variable 
with a python keyword.
"""
class_ = 10
