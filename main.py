
def f(n):
    if n < 0:
        return "Not valid!"        
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return f(n - 2) + f(n - 1)

print(f(int(input("Number: "))))