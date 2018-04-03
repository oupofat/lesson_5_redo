'''Exercise 8
Extend your solution to exercise 7 to to convert text surrounded by underscores (_) to yellow. So This Sunday the _Browns_ are playing vs the *Reds*. should convert to This Sunday the \033[33mBrowns\033[0m are playing vs the \033[31mreds\033[0m. In the terminal (not not in Python Tutor) the word Brown should be in yellow.'''


user = "So This Sunday the _Browns_ are playing vs the *Reds*."
sentence = ""
state = "open"

for letter in user:
    if state == "open":
        if letter == "_":
            state = "underscore"
            sentence += "\033[33m"
        elif letter == "*":
            state = "red"
            sentence += "\033[31m"
        else:
            sentence += letter
    elif state == "underscore":
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
        