def sorting(x):
    for i in range(len(x)-1):
        if x[i] <= x[i+1]:
            pass
        else:
            return False
    return True

def bubbleSort(listData):
    Iterasi = {'kiri':0, 'kanan':0}
    print('Data yang akan diurutkan : ',listData)
    count=0
    if sorting(listData) == False:
        for outIter in range(len(listData)-1,-1,-1):
            if sorting(listData) == False:
                count=count+1
                print ('Iterasi ke - ', count,' : ')

                print('Sorting dari kiri ke kanan :')
                for i in range(outIter):
                    if listData[i]>listData[i+1]:
                        temp=listData[i]
                        listData[i]=listData[i+1]
                        listData[i+1]=temp
                        print(listData)
                        Iterasi['kiri'] += 1

                if sorting(listData) == False:
                    print('Sorting dari kanan ke kiri :')
                    for j in range(outIter, 0, -1):
                        if listData[j] < listData[j-1]:
                            temp = listData[j]
                            listData[j] = listData[j-1]
                            listData[j-1] = temp
                            print(listData)
                            Iterasi['kanan'] += 1
            else:
                pass    
        
        print('='*40)
        print('Data urut - ',listData)
        print('Total Iterasi Kiri ke Kanan adalah : ',Iterasi['kiri'])
        print('Total Iterasi Kanan ke Kiri adalah : ',Iterasi['kanan'])
        print('---------------------------------------')
    else:
        print('Tidak ada iterasi lagi karena data sudah urut : ',listData)

listData = [10,2,5,8,1,20,2,2,4]
bubbleSort(listData)