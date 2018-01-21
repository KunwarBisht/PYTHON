##exceptions_raise

class ShortInput(Exception):
    def __init__(self,length,atleast):
        Exception.__init__(self)
        self.length=length
        self.atleast=atleast



try:
    getString=input("Please ente any string:")

    if len(getString)<3:
        raise ShortInput(len(getString),3)

except EOFError :
    print("EofError")

except ShortInput as ex:
    print("ShortInput Exception. the input was {} long and expected {} atleast".format(ex.length,ex.atleast))

else :
    print("no exception was raised")
