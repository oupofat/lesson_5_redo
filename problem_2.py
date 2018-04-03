'''2. Convert to HTML Part 2
Take your solution in 1 and extend it so that you also convert text surrounded by the $ symbol to be surrounded by the <strong> tag. Example: I loves me some $bling bling$. should convert to I loves me some <strong>bling bling</strong>.'''


user = "I love me some $bling bling$."
sentence = ""
state = "open"

for letter in user:
    if state == "open":
        if letter == "$":
            state = "strong"
            sentence += "<strong>"
        else:
            sentence += letter
        
    elif state == "strong":
        if letter == "$":
            state = "open"
            sentence += "</stong>"
        else:
            sentence += letter
print (sentence)
        