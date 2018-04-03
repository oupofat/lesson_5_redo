'''4. Remove parenthesized text
Take your solution in #3 and extend it to remove any text surrounded by parenthesis. For example: The touch of her lips (we had just a wondrous kiss) was heaven. should convert to The touch of her lips was heaven.

Hint: when you are in the "in-parenthesis" state, what would would you do to accumulate to the accumulator variable, if anything?'''

user = "The touch of her lips (we had just a wondrous kiss) was heaven."
sentence = ""
state = "open"
for letter in user:
    if state =="open":
        if letter == "(":
            state = "blank"
            sentence += ("")
        else:
            sentence += letter
    elif state == "blank":
        if letter == ")":
            state = "open"
            sentence += ("")
        else:
            "pass"
print(sentence)
        
