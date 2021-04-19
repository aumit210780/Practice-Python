n = int(input())
for i in range(2,n):
    if n%i == 0:
        print("Composite")
        break
else:
    print("Prime")