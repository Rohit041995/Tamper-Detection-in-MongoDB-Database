import glob
import hashlib

filenames = glob.glob("*.txt")
f = open("hash.txt", "a")
for filename in filenames:
    with open(filename, 'rb') as inputfile:
        data = inputfile.read()
        print(filename, hashlib.md5(data).hexdigest())
        s=filename
        s1=hashlib.md5(data).hexdigest()
        s=s+": "+s1+"\n"
        f.write(s)
f.close()        
