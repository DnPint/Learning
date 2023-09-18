import time

def count(end,start=1):
    for i in range(start,end+1):
        print(i)
        time.sleep(1)
    print("Done!")

count(5)