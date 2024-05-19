x = int(input("Enter the number : "))
y = int(input("Enter the number : "))
z = int(input("Enter the number : "))

print(x) if x>=y and x>=z else ( print(y) if y>=x and y>=z else print(z) )