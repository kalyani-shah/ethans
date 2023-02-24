try:
    num=int(input('enter a number:'))
    l1=[1,2,3,4]
    print(3/num)
    import abcde
    print(l1[6])
except IndexError as E:
    print('I am in index error block')
    print(E)
except ImportError as E:
    print('I am in import block')
    print(E)
except ZeroDivisionError as E:
    print(E)
    print('ABC')
except Exception as E: #generic exception.
    print(E)
    print('generic')
else:
    print('no exception')
finally:
    print('cleanup process')