try:
    mylist=[1,2,3,4,5]
    assert 1,2 in mylist
    print(mylist)
    mylist.pop()
    print(mylist)
    assert len(mylist) >=1

except AssertionError:
    print("condition false")

else :
    print("np exceptio")

'''
The assert statement is used to assert that something is true. For example,
if you are very sure that you will have at least one element in a list you are using and want to check this,
and raise an error if it is not true, then assert statement is ideal in this situation.
When the assert statement fails, an AssertionError is raised. The pop() method removes and returns the last item from the list.
'''
