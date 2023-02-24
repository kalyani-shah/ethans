#Furthermore, a function can return another function.
'''
Here, is_returned() is a nested function which is defined
and
returned each time we call is_called().
'''
def is_called():
    def is_returned():
        return "Hello"
    return is_returned

if __name__=='__main__':
    new = is_called() #new --> is_returned
    print(new())

    #new and is_returned--> same memory location