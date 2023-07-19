arr = [3,30,34,5,9]
n=len(arr)
for i in range(n):
    arr[i]=str(arr[i])
for i in range(n):
    for j in range(i+1,n):
        if arr[j]+arr[i]>arr[i]+arr[j]:
            arr[i],arr[j]=arr[j],arr[i]

print("".join(arr))