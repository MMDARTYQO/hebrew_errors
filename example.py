from hebrew_errors import print_hebrew_error

try:
    x = 1 / 0
except Exception as e:
    print_hebrew_error(e)