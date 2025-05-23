from hebrew_errors import print_hebrew_error

try:
    x = 1 / 0
except Exception as e:
    print_hebrew_error(e)

try:
    x = 'text' + 1
except Exception as e:
    print_hebrew_error(e)

try:
    from math import non_existent_name_in_math_module
except Exception as e:
    print_hebrew_error(e)

try:
    eval("invalid$char = 1")
except Exception as e:
    print_hebrew_error(e)

try:
    eval("'unterminated string")
except Exception as e:
    print_hebrew_error(e)

try:
    eval("print(")
except Exception as e:
    print_hebrew_error(e)

try:
    x = +'a'
except Exception as e:
    print_hebrew_error(e)

try:
    eval("print 'hello'")
except Exception as e:
    print_hebrew_error(e)