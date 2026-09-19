log=[
    "2026-08-18 10:01:01 INFO UserService Request successful",
    "2026-08-18 10:01:05 INFO UserService Request successful",
    "2026-08-18 10:02:10 ERROR UserService Database timeout",
    "2026-08-18 10:02:11 ERROR UserService Database timeout",
    "2026-08-18 10:02:12 ERROR UserService Database timeout",
    "2026-08-18 10:02:13 ERROR UserService Database timeout",
    "2026-08-18 10:03:01 INFO UserService Request successful",
]
info=0
error=0
limit=3

for line in log:
    word=line.split()
    time=word[1]
    status=word[2]
    service=word[3]

    if status=="ERROR":
        error=error+1
        print("Alert",time,status,service)
    elif status=="INFO":
        info=info+1
        print("Normal",time,status,service)

print("Total INFO messages:", info)
print("Total ERROR messages:", error)

if(error>limit):
    print("ALERT: Error messages exceeded the limit of", limit)
else:
    print("INFO: Error messages are within the limit of", limit)
