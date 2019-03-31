from datetime import datetime
from time import sleep


"""
example: 1
"""
def log(message, when=datetime.now()):
    # when will always be same for each call
    print(message, when)



log("hi")
#sleep(5)
log("bye")


"""
example: 2
"""

def add(x, items=[]):
    items.append(x)
    return items


print(add(12))
print(add(34))
