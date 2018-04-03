user = "I like to program in [Python:34] and [HTML:32]"

sentence = ''
color_word = ''
code_color = ''
state = "open"

for letter in user:
    if state == "open":
        if letter == "[":
            state = "colon"
            color_word += "\033[%dm"  
        elif "[" not in letter:
            sentence += letter
        else:
            sentence += letter
    elif state == "colon":
        if  letter == ":":
            state = "open_colon"
            color_word += "\033[0m"
        elif ":" not in letter:
            color_word += letter
        else:
            sentence += letter
    elif state == "open_colon":
        if letter != ":" and letter != "]":
            code_color += letter
        else:
            sentence += letter
            state = "open"
print(sentence)