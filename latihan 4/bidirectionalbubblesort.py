#setelah dimodifikasi dengan bidirectional bubble sort 
#dan jika data sudah terurut iterasi berhenti
a=[10,6,7,1,10,12,100,1,0,23,45,7,8,9,0]
jalan=True
count=1
while jalan:
    i=len(a)-1
    check=True
    print("iterasi ke-",count)
    for j in range(i):
        if a[j]>a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]
            check=check and False
        else:
            check=check and True
        if check==False:
            print(a)

    for k in range(i,0,-1):
        if a[k]<a[k-1]:
            a[k],a[k-1]=a[k-1],a[k]
            check=check and False
        else:
            check=check and True
        if check==False:
            print(a)
    i-=1
    if check==False:
        count+=1
        continue
    else:
        print("tidak ada iterasi dalam lagi karena data sudah terurut")
        jalan=False

print("data terurut: ",a)