inFp = open("C:/Temp/data1.txt","r")

line = inFp.readline()
while True:
    line = inFp.readline()
    if not line : break
    print(line)
inFp.close()
