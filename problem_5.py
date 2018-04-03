'''Exercise 5
Ask the user for a code, and then print "Hello world" with that code as the control code.'''

code = 35
print ("\033[%dmHello world\033[0m" % code)