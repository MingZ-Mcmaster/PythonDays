__author__="Ming"

def add(a, b, f):
    return f(a)+f(b)

res = add(3, -6, abs)
print(res)