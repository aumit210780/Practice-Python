print("And Operation >>>>>>>>>>>")
s = int(input())
e = int(input())
if (s+e)<10 and s>0:
    print("Possible for and")
    print()
else:
    print("Impossible for and")
    print()

print("Or Operation >>>>>>>>>>>>>")
st = int(input())
en = int(input())
if (st+en)<10 or st>0:
    print("Possible for or")
else:
    print("Impossible for or")