'''Exercise 6
Ask the user for a code, and the text message, to print. Print that message using that control code.'''


code = 34
message = "This is a test text"
print ("\033[%dm, %s\033[0m" % (code,message))