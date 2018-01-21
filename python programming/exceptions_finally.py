import sys
import time
poem='''\ hello how are you!!
doing good.
great'''

fileOp=open("poem.txt","w")
fileOp.write(poem)
fileOp.close()

f=None
try:
    f=open("poem.txt")
    #our usual file-reading idiom
    while True:
        line=f.readline()
        if len(line)==0:
            break
        print(line,end='')
        sys.stdout.flush()

        print("press ctrl +c now")

        time.sleep(2)
except IOError:
    print("could not find file Poem.txt")
except KeyboardInterrupt:
    print("!!You cancelled the reading from the file")

finally:
    if f:
        f.close()
        print("closing the file")
        
