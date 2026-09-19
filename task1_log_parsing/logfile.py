file=open("log.txt","r")
eroor=0
info=0
limit =3

for line in file:
    word=line.split()
    time=word[1]
    status=word[2]
    service=word[3]

    if status=="ERROR":
        eroor=eroor+1
        print("Alert",time,status,service)
    elif status=="INFO":
        info=info+1
        print("Normal",time,status,service)

file.close()
print("Total INFO messages:", info)
print("Total ERROR messages:", eroor)

if(eroor>limit):
    print("ALERT: Error messages exceeded the limit of", limit)
else:
    print("INFO: Error messages are within the limit of", limit)