import queueProgram as qp #Digunakan untuk import file lain yang berisi fungsi queue 

def onproses(antrian): #Onproses digunakan untuk membuat jumlah antrian suatu proses jumlah antrian cpu.
    total=antrian #membuat variabel baru yang bisa digunakan untuk menampung inputan jumlah antrian cpu.
    for x in range(total): 
        name_time=[] #digunakan untuk menampung list dari task dan waktu yang dibutuhkan untuk menggunakan cpu.
        name=str(input('Nama Proses ke - '+str(x)+' = ')) ##digunakan untuk menginputkan berupa string. 
        name_time.append(name) #digunakan untuk menambahkan item ke akhir daftar list.
        time=int(input('Waktu Proses = '))  #digunakan untuk menginputkan waktu yang akan digunakan dalam menggunakan cpu.
        name_time.append(time)
        qp.enqueue(Q,name_time) #digunakan untuk menambahkan suatu item baru ke ujung satu antria.
    print("")
        
def proses(key,val): #digunakan untuk proses antrian cpu sebagai lanjutan dari onproses. 
    x=0
    temp=0
    while qp.size(Q)>=0: #size untuk menjumlahkan data yang terdapat pada queuee.
        if qp.size(Q)==0:
            break
        elif x>=qp.size(Q):
            x=0
        else:
            temp+=1
            print('Iterasi ke - ',temp)
            Q[-(1)][1]=Q[-(1)][1] - val
            if Q[-(1)][1]<=0:
                print('          Proses '+Q[-(1)][0]+'   telah selesai diproses')
                qp.dequeue(Q) #menghapus item depan antrian.
            elif Q[-(1)][1]>0:
                print('          Proses '+Q[-(1)][0]+'   sedang diproses, dan sisa waktu proses '+Q[-(1)]\
                      [0]+" = "+str(Q[-(1)][1]))
                qp.enqueue(Q,qp.dequeue(Q))                
            x+=1
            print('          Data proses yang tersisa : ',Q)
            

Q=qp.createQueue() #membuat antrian baru queue dengan jumlah elemen kosong.
onoperasi=int(input('Jumlah Proses yang akan dijadwalkan di CPU = '))
print('--------------------------------------------')
onproses(onoperasi)
print('---------------------------------')
operasi=int(input('Waktu proses CPU = '))
print('---------------------------------')
print("Antrian Proses = ",Q)
proses(Q,operasi)