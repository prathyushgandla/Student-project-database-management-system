'''size=int(input())
lst=list(map(int,input().split(',')))
lst.sort()
a=0
for i in range(1,size-1):
    if lst[a]%2==0:
        if lst[i]%2==0:
            lst[i],lst[i+1]=lst[i+1],lst[i]
        a+=1
    elif lst[a]%2!=0:
        if lst[i]%2!=0:
            lst[i],lst[i+1]=lst[i+1],lst[i]
        a+=1
print(lst)

val=input()
lst=[]
for i in val:
    lst.append(val.count(i))
res=max(lst)
for i in val:
    if val.count(i)==res:
        print(i)
        break

n=int(input())
arr = list(map(int,input().split()))
d=int(input())
def rotate(arr,d,n):
    first=arr[0]
    for i in range(n-1):
        some=arr[i]
        arr[i]=arr[i+1]
    arr[-1]=first

for i in range(d):
    rotate(arr,d,n)
print(arr)
a,b=input().split()
cnt,res=0,0
arr=[]
while(res<=int(b)):
    for i in range(2,int(a)+1):
        if int(a)%i==0:
            cnt+=1
    if cnt==1:
        res+=1
    a=int(a)+1
    print(a)

arr=[1,2,3,3,4]
new=[]
for i in range(len(arr)-1):
    res=abs(arr[i]-arr[i+1])
    new.append(res)
print(sum(new))
s='5+x=7'
if s.index('+')==s.index('x')+1:
    val=abs(int(s[-1])-int(s[0]))
elif s.index('x')==s.index('+')+1:
    val=s[int(s.index('x'))-int(s[-1])]
z=s.replace('=','')
y=z.replace('x','')
print(s)
a,b=y.split('+')
val=int(a)+int(b)
print(val)
n=list(input().split())
for i in n:
    print(i)
x=input()
n=list(input().split())
a=input()
if a in n:
    print("Book is available in position number:",end="")
    print(n.index(a)+1)
else:
    print("Book not available")
'''
r= int(input())
n= int(input())
arr=[]
for i in range(n):
    a=int(input())
    arr.append(a)
if n==0:
    print("NA")
if r>arr[0]:
    for i in range(arr[0]+1,n+1):
        print(i,"",end="")
else:
    for i in range(1,n+1):
        print(i,"",end="")
