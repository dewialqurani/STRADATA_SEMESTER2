import queueProgram as qp 
                            


def buat_antrian(jumlah_antrian_di_cpu):
    jum=jumlah_antrian_di_cpu
    for i in range(jum):
        nama_dan_waktu=[]
        nw=nama_dan_waktu
        nama_proses=str(input("Nama Proses ke -"+str(i)+" : "))
        #nama_proses="A"
        nw.append(nama_proses)
        waktu_proses=int(input("Waktu Proses : "))
        #waktu_proses=3
        nw.append(waktu_proses)
        qp.enqueue(Q,nw)
    print("")
        
def proses_antrian_cpu(antrian_queue,waktu_proses_cpu):
    aq=antrian_queue
    wpc=waktu_proses_cpu
    i=0
    buat_tanda_iterasi=0
    while qp.size(Q)>=0:
        if qp.size(Q)==0:
            break
        elif i>=qp.size(Q):
            i=0
        else:
            buat_tanda_iterasi+=1
            print("Iterasi ke- ",buat_tanda_iterasi)
            Q[-(1)][1]=Q[-(1)][1] - wpc
            if Q[-(1)][1]<=0:
                print("Proses "+Q[-(1)][0]+" telah selesai diproses")
                qp.dequeue(Q)
            elif Q[-(1)][1]>0:
                print("Proses "+Q[-(1)][0]+" sedang diproses, dan sisa waktu proses "+Q[-(1)]\
                      [0]+" = "+str(Q[-(1)][1]))
                qp.enqueue(Q,qp.dequeue(Q))                
            i+=1
            print("Data proses yang tersisa : ",Q)
            print("")
            

Q=qp.createQueue()

jumlah_proses=int(input("Jumlah Proses yang akan dijadwalkan di CPU = "))
print("")

buat_antrian(jumlah_proses)

waktu_proses_di_cpu=int(input("Waktu proses CPU = "))
print("")
wc=waktu_proses_di_cpu

print("Antrian Proses beserta waktunya = ",Q)
print("")

proses_antrian_cpu(Q,wc)
#for j in range (qp.size(Q)):
    #Q[j][1]-=1

    
