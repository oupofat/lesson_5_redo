'''Exercise 9
Extend your solution to exercise 8: one more color code to the above --- text surrounded by dollar signs ($) should be displayed in green.'''

user = "So This Sunday the _Browns_ are playing vs the *Reds* after they plat the $Green Bay Packer$."

sentence = ""
state = "open"

for letter in user:
    if state == "open":
        if letter == "_":
            state = "yellow"
            sentence += "\033[33m"
        elif letter == "*":
            state = "red"
            sentence += "\033[31m"
        elif letter == "$":
            state = "green"
            sentence += "\033[32m"
        else:
            sentence += letter
    elif state == "yellow":
        if letter == "_":
            state = "open"
            sentence += "\033[0m"
        else:
            sentence += letter
    elif state == "red":
        if letter == "*":
            state = "open"
            sentence += "\033[0m"
        else:
            sentence += letter
    elif state == "green":
        if letter == "$":
            state = "open"
            sentence += "\033[0m"
        else:
            sentence += letter
print (sentence)