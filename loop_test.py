
for x in range(10):
    print(x)
else:
    print("else:1")

for x in []:
    print(x)
else:
    print("else:2")



for x in range(10):
    break
else:
    print("else:3")


def call_return():
    for x in range(11):
        return
    else:
        print("else: 4")
