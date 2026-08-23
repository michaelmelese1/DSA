# a = 5
# b = "hello"
# print(f"{b} {a**6} {a+1}")

# a = "hello world"

# print("world" in a)

# b = "Hello, World"
# print(b[2])
# print(b[-3])
# print(b[2:5])
# print(b[:5])
# print(b[2:])
# print(b[5:2:-1])
# print(b[::-1])
# print(b[::2])

# fruits = ["apple", "banana", "orange"]

# print(fruits[0])

# for fruit in range(len(fruits)):
#     if fruit == "banana":
#         print("Found banana!")
#         break 
#     else:
#         print("banana not found in the list.")
# for num in range(10,14):
#     for i in range(2, num):
#         if num % i == 1:
#             print(num)
#             break

def evenChecker(n):
    if n % 2 == 0:
        print("even")
    else:
        print("Odd")
        n = 2