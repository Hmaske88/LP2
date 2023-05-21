List=[(job,deadline,profit) for job,deadline,profit in zip(map(str,input("Enter the jobs separated by space :").split(" ")),map(int,input("Enter the respective deadlines separated by space :").split(" ")),map(int,input("Enter the respective profits separated by space :").split(" ")))]
print(List)
# List=[('j1', 3, 4), ('j2', 1, 5), ('j3', 1, 3)]

L=sorted(List,key= lambda x:x[2], reverse=True)

slot=[]
ans=[]

for i in range(len(L)):
    slot.append(0)
    ans.append('null')
    
profit=0

for i in range(len(L)):
    job=L[i]
    for j in range(job[1],0,-1):
        j=j-1
        if slot[j]==0:
            slot[j]=1
            ans[j]=job[0]
            profit+=job[2]
            break
    
print("Profit = ",profit)
n=1
for i in ans:
    print("Slot",n," --> ",i)
    n+=1
