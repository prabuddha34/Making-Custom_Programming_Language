import  basic
while True:
    text=input('PraxyCompili >')
    print(text)
    tokens, errors =basic.run(text)

    if errors:print(errors.as_string())
    else : print(tokens)
    #We have to make a lexer