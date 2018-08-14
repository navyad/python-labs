# ====================
z = 0
def outer():
    z = 1
    def inner():
        z = 2
        print("inner:", z)

    inner()
    print("outer:", z)

outer()
print("global:", z)
# ====================
x = 0
def outer():
    x = 1
    def inner():
        global x
        x = 2
        print("inner:", x)

    inner()
    print("outer:", x)

outer()
print("global:", x)

# =====================
p = 0
def outer():
    p = 1
    def inner():
        nonlocal p
        p = 2
        print("inner:", p)

    inner()
    print("outer:", p)

outer()
print("global:", p)



# ========================
k = 0
def k_outer():
    def k_inner():
        nonlocal k
        k = 10

k_outer()

