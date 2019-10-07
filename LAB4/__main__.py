import time
ifile = open('reut2-0000.sgm', 'rb')
data = ifile.read(1024)
while data:
    ofile = open(str(time.time()) + '.txt', 'wb')
    ofile.write(data)
    ofile.close()
    data = ifile.read(1024*1024*1024*1024)
ifile.close()
