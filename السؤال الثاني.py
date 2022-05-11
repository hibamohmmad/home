H=int(input("H="))
t=res=0
while H!=0:
    res=res+(H%2)*(10**t)
    H=H//2
    t+=1
print(f"the binary number= (res)")
