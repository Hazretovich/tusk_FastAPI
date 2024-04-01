import time
import sys

if len(sys.argv) > 1:
    value = sys.argv[1]
else:
    value = 0
working = True

while working:
    time.sleep(1)
    print(value)
    value+=1
