'''Closures:A Closure is a function object that remembers
 values
in enclosing
scopes even if they are not present in memory.
'''
def multiplier_of(n):
    def multiplier(number):
        return number*n
    return multiplier

multiplywith5 = multiplier_of(5) #number*5  --> multiplier 5*number
print(multiplywith5)
print(multiplywith5(9))
print(multiplywith5(10))