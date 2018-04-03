'''Exercise 7
Ask the user for a text message with optional asterisks (*) in them to surround phrases or words. Convert the part inside the asterisk to red. So: Pass me the *french fries*! should convert to Pass me the \033[31mfrench fries\033[0m. In the terminal (not in Python Tutor) the french fries should look red.'''

user = "Pass me the *french fries*!"
sentence = ''
state = "open"
for letter in user:
    if state == "open":
        if letter == "*":
            state = "red"
            sentence += "\033[31m"
        else:
            sentence += letter
    elif state == "red":
        if letter == "*":
            state = "open"
            sentence += "\033[0m"
        else:
            sentence += letter
            
print(sentence)