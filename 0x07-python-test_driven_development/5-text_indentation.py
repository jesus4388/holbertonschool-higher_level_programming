#!/usr/bin/python3
'# that prints a text with 2 new lines after each\
        of these characters: ., ? and :'


def text_indentation(text):
    '# that prints a text with 2 new lines after each\
            of these characters: . ? and :'
    flag = False
    if not text:
        raise TypeError('text must be a string')
    if not isinstance(text, str):
        raise TypeError('text must be a string')
    new = text.replace(". ", ".")
    new = new.replace(": ", ":")
    new = new.replace("? ", "?")
    new = new.strip(" ")
    for char in new:
        if char in [".", "?", ":"]:
            print(char)
            print()
            flag = True
        else:
            if flag is False:
                print(char, end="")
            else:
                if char != " ":
                    print(char, end="")
                    flag = False
