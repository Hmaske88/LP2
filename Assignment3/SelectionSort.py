l=list(map(int,input("Enter elements in an array separated by space :").split(" ")))

for i in range(len(l)):
    for j in range(i+1,len(l)):
        if(l[i]>l[j]):
            l[i],l[j]=l[j],l[i]
print(l)
