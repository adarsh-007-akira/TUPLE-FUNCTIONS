num=int(input("Number of Intgers :\t"))
tup=()
lst=list(tup)
for i in range(num):
    b=[]
    a=input("\tEnter the value :\t")
    c=int(a)**3
    b.append(a)
    b.append(str(c))
    lst.append(b)
tup=tuple(lst)
print(tup)