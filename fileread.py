#fileHandle1 = open("C:\Users\IBM_ADMIN\Documents\Python Scripts\Write",'r')
#linecnt=0
#for fileLine in fileHandle1:
#    print ("line : " , fileLine)
#    linecnt+=1

try:
    handle=open("C:\Users\IBM_ADMIN\Documents\Python Scripts\Write2",'r')
 
except:
    print "open failed"
    exit()

in1=handle.read()
print in1
fileHandle1.close()


