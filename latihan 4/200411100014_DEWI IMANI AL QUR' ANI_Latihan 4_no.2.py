b=[10,2,5,8,1,20,2,2,4]
urutan=True
count=1
while urutan:
    i=len(b)-1
    pilih=True
    print('iterasi ke - ',count)
    for j in range(i):
        if b[j]>b[j+1]:
            b[j],b[j+1]=b[j+1],b[j]
            pilih=pilih and False
        else:
            pilih=pilih and True
        if pilih==False:
            print(b)

    for k in range(i,0,-1):
        if b[k]<b[k-1]:
            b[k],b[k-1]=b[k-1],b[k]
            pilih=pilih and False
        else:
            pilih=pilih and True
        if pilih==False:
            print(b)
    i-=1
    if pilih==False:
        count+=1
        continue
    else:
        print('-------------------------------------')
        print('Tidak ada iterasi lagi karena data sudah urut ')
        urutan=False
print('-------------------------------------')
print('Data yang sudah urut : ',b)