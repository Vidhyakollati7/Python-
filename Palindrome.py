a = input("Enter a string").lower().replace(" ","")
b = a[::-1]
print(b)
if b == a:
    print("It is a palindrome:", b)
else:
    print("Not a palindrome")