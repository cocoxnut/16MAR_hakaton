info = input("Write code for Python for reverse list: 1, 2, 3, 4, 5 ")[::-1]
try:
    info = int(info)
    print(info)
except:
    print("STR is not allowed")

