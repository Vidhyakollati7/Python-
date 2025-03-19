i=int(input())
if i % 2==0:
    if i % 4==0:
        print(i)
    else:
        print("Even number,but not multiple of 4")
else:
        if i % 3==0:
            print(i)
        else:
            print("Odd number,but not multiple of 3")