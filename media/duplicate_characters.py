'''s=list(input())
st=[]
i=0
while i<len(s):
    if i==len(s)-1:
        break
    else:
        if s[i]==s[i+1]:
            del s[i:i+2]
            i=0
        elif s[i]!=s[i+1]:
            if len(s)<=2:
                break
            else:
                i+=1
print(''.join(i for i in s))
while i<len(s):
    if len(st)!=0 and st[-1]==s[i]:
        i+=1
        st.pop(-1)
    else:
        st.append(s[i])
        i+=1
print(''.join(i for i in st))
def GetLongestStreak(a,b):
    count1,count2,count3=0,0,0
    arr1=[]
    r = a^b
    m = a*b
    a = a+b
    x=format(r,'b')
    y=format(m,'b')
    z=format(a,'b')
    for i in range(len(x)-1):
        if x[i]==x[i+1]:
            count1+=1
    for i in range(len(y)-1):
        if y[i]==y[i+1]:
            count2+=1
    for i in range(len(z)-1):
        if z[i]==z[i+1]:
            count3+=1
    arr=[count1,count2,count3]
    for i in arr:
        arr1.append(arr.count(i))
    return '1'*max(arr1)
a1=int(input())
b1=int(input())
result=GetLongestStreak(a1,b1)
print(result)
def solve(N):
    a=2**N
    res=len(str(a))
    b=0
    while res>1:
        b=0
        for i in str(a):
            b+=int(i)
        res=len(str(b))
        a=b
    return b 
T=int(input())
for i in range(T):
    N=int(input())
    out=solve(N)
    print(out)
N=2
a=2**N
res=len(str(a))
b=a
while res>1:
    b=0
    for i in str(a):
        b+=int(i)
    res=len(str(b))
    a=b
print(b)'''
r= int(input())
n= int(input())
arr=[]
for i in range(9):
    arr.append(int(input())
if n=='0':
    print("NA")
elif r>arr[0]:
    for i in range(arr[0],n+1):
        print(i,end="")
else:
    for i in range(1,n+1):
        print(i,end="")
