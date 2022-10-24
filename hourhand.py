print("*"*20)
print("Minutes Converter")
print("*"*20)
m=float(input("Enter Minutes\n"))
while m>60 and m<=110:
    rm=m-60
    print("1 hour",rm,"minutes")
    break
else:
    tm=m/60
    tmd=tm%1
    tmw=tm//1
    tmd=tmd*60
    if tmw>0:
        print("%.0f"%tmw,"Hours")
    if tmd>0:
        print("%.0f"%tmd,"Minutes")






