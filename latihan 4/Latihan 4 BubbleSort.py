def sorting(a):
    for i in range(len(a)-1):
        if a[i] <= a[i+1]:
            pass
        else:
            return False
    return True

def bubbleSort(listData):
    iteration = {'it_kiri':0, 'it_kanan':0}
    print('Data yang akan diurutkan :',listData)
    count=0
    if sorting(listData) == False:
        for outIter in range(len(listData)-1,-1,-1):
            if sorting(listData) == False:
                print('\n')
                count=count+1
                print ('Iterasi ke-', count,':')

                print('Pointer dari kiri ke kanan :')
                for i in range(outIter):
                    if listData[i]>listData[i+1]:
                        temp=listData[i]
                        listData[i]=listData[i+1]
                        listData[i+1]=temp
                        print(listData)
                        iteration['it_kiri'] += 1

                print('')

                if sorting(listData) == False:
                    print('Pointer dari kanan ke kiri :')
                    for j in range(outIter, 0, -1):
                        if listData[j] < listData[j-1]:
                            temp = listData[j]
                            listData[j] = listData[j-1]
                            listData[j-1] = temp
                            print(listData)
                            iteration['it_kanan'] += 1
            else:
                pass    
        
        print('')
        print('='*40)
        print('Data urut-',listData)
        print('Total Iterasi Kiri  => Kanan : ',iteration['it_kiri'])
        print('Total Iterasi Kanan => Kiri  : ',iteration['it_kanan'])
        print('')
    else:
        print('\nMaaf, namun data sudah urut:',listData)

listData = [10,2,5,8,1,20,2,2,4]
bubbleSort(listData)

# NAMA   : A. TEGUH BUDI SETYA PRASETYA
# NIM    : 200411100144
# KELAS  : STRUKTUR DATA A