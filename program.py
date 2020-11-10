a = input("write your first number")
b = input("write your second number")
if ((a[-1]==b[-1] or a[-2]==b[-2]) & ((int(a)%2==0) & (int(b)%2==0))):
    print("This is a mecha number")
else:
    print("This is not mecha number")
 
