def powersum(power,*args):
    total=0
    for i in args:
        total +=pow(i,power)

    return total

print(powersum(2,3,4,5))

'''
Because we have a * prefix on the args variable, all extra arguments passed to
the function are stored in args as a tuple.
If a ** prefix had been used instead, the extra parameters would be
considered to be key/value pairs of a dictionary.
'''

