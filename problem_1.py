'''1. Convert to HTML
Convert text to HTML. Ask the user to input a sentence. Convert words surrounded by asterisks to be surrounded by the <em> tag </em>. (The requirement is same as in the lecture slides, please do it yourself)'''


user = "this is the first *time in* redoing this!"
new_sentence = ''
state = "open"

for letter in user:
    if state == "open":
        if letter == "*":
            state = "emphasis"
            new_sentence += "<em>"
        else:
            new_sentence += letter
    elif state == "emphasis":
        if letter == "*":
            state = "open"
            new_sentence += "</em>"
        else:
            new_sentence += letter
print (new_sentence)