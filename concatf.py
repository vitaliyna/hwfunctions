def concat(*args,reversed = False):
    y = ''
    if reversed == True:
        for x in args[::-1] :
            y = y + x
    else: 
        for x in args:
            y = y + x
    return (y)

print(concat('hello', ' ', 'world', '!',reversed = False))