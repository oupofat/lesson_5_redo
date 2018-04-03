'''3. Capitalize asterisked text
Ask the user to input a sentence. Convert any text surrounded by asterisks to upper case. For example: I *love* hamburgers. should convert to I LOVE hamburgers.'''

user = "I *love* hamburgers."
sentence = ""
upper =  ""
state = "open"
for letter in user:
    if state == "open":
        if letter =="*":
            state = "upper"
            sentence += upper
        else:
            sentence += letter
    elif state =="upper":
        if letter =="*":
            state = "open"
            sentence += upper
        else:
            sentence += letter.upper()
print (sentence)