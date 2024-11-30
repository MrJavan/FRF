from clear import clear
clear()
# x = -2
# y = -1
# c = 0 
# n = 3
# x = -1

# def first(n):
#     if n != x:
#         c += 1
#         return first(n - 1)
#     else:
#         print(n + 2)
#         print(c)
#         return n + 2

# def second(n):
#     if n != y:
#         return second(n - 1)
#     else:
#         print(n + 1)
#         return n + 1

def f(n):
    if n == 0:
        return 0
    elif n == -1:
        return 1
    else:
        return f(n - 2) + f(n - 1)

print(f(9))
     