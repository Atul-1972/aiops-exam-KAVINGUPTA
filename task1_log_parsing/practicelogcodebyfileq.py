file=open("log.txt","r")
info=0
error=0
limit=1
for line in file:
    word=line.split()
    time=word[1]
    status=word[2]
    service=word[3]

    if(status=="ERROR"):
        error=error+1
        print("Alert",time,status,service)
    elif(status=="INFO"):
        info=info+1
        print("Normal",time,status,service)

file.close()
print("Total INFO messages:", info)
print("Total ERROR messages:", error)
if(error>limit):
    print("ALERT: Error messages exceeded the limit of", limit)
else:
    print("INFO: Error messages are within the limit of", limit)

