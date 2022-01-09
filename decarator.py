def inspact(func):
    def inner(*args, **kwargs):
        print('Args:', args)
        print('Kwargs:',kwargs)        
        print("Return value:", func(*args, **kwargs))
        print(func(*args, **kwargs))
    return inner

@inspact
def concat(*args,reverse = False):
    y = ''
    if reverse == True:
        for x in reversed(args):
            y = y + x
    else: 
        for x in args:
            y = y + x
    return (y)

print(inspact(concat('hello', ' ', 'world', '!', reverse = True)))
