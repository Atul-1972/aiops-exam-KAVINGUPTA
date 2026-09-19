log=[
    "2026-08-18 10:01:01 INFO UserService Request successful",
    "2026-08-18 10:01:05 INFO UserService Request successful",
    "2026-08-18 10:01:09 INFO UserService Request successful",
    "2026-08-18 10:01:15 INFO UserService Request successful",
    "2026-08-18 10:02:01 INFO UserService Request successful",
    "2026-08-18 10:02:05 INFO UserService Request successful",
    "2026-08-18 10:02:10 ERROR UserService Database timeout",
    "2026-08-18 10:02:11 ERROR UserService Database timeout",
    "2026-08-18 10:02:12 ERROR UserService Database timeout",
    "2026-08-18 10:02:13 ERROR UserService Database timeout",
    "2026-08-18 10:02:14 ERROR UserService Database timeout",
    "2026-08-18 10:03:01 INFO UserService Request successful",
    "2026-08-18 10:03:05 INFO UserService Request successful",
    "2026-08-18 10:03:09 INFO UserService Request successful",
    "2026-08-18 10:04:10 ERROR UserService Database timeout",
    "2026-08-18 10:04:11 ERROR UserService Database timeout",
    "2026-08-18 10:04:12 ERROR UserService Database timeout",
    "2026-08-18 10:04:13 ERROR UserService Database timeout",
    "2026-08-18 10:04:14 ERROR UserService Database timeout",
    "2026-08-18 10:04:14 ERROR UserService Database timeout",
    "2026-08-18 10:04:14 ERROR UserService Database timeout"
]
info=0
error=0
limit=5

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

print("Total INFO",info)
print("Total ERROR",error)

if(error>limit):
    print("The error rate are passed the set limit",limit)
else :
    print("The error rate are within the set limit",limit)


