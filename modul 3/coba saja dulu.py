def createQueue():
    q = []
    return q
def enqueue(q,data):
    q.append(data)
    return(q)
def dequeue(q):
    data = q.pop(0)
    return(data)
def isEmpty(q):
    return(q == [])
def size(q):
    return(len(q))


def proses():
    jumlah_data = int(input("Jumlah Proses yang akan dijadwal di CPU : ")) #sebagai jangkauan data di dalam list data
    storage = createQueue()
    for f in range(jumlah_data): #Mmbuat list data yang akan diproses ke dalam CPU
        temp = createQueue()
        for g in range(1):
            nama = input("Nama Proses ke-{}: ".format(f))
            waktu = input("Waktu proses : ")
            enqueue(temp,nama.upper())
            enqueue(temp,waktu)
        enqueue(storage,temp)

    alphabet = "ABCDEFGHIJKLKMNOPQRSTUVWXYZ"
    n = size(storage)
    key = createQueue()
    val = createQueue()
    for x in range(n): #Memilah data didalam data inputan
        for y in range(2):
            char_data =  storage[x][y]
            if char_data in alphabet : # jika setiap elemnt storage berupa alphabet maka akun masuk kedalam queue key
                enqueue(key,char_data)
            else: # jika setiap elemnt storage selain alphabet maka akun masuk kedalam queue key
                enqueue(val,int(char_data))
    print("Antrian Proses beserta Waktunya:\n Data: {}\n Waktu: {}\n".format(key,val))
    num_iter = 1
    while size(key) > 0 :
        for j in range(size(val)):
            if val[0] >= 3 : #Jika nilai di dalam queue melibihi time proses
                obj = key[0]
                operasi = val[0] - 3 #operasi untuk mengurasi waktu setiap key
                val[0] = operasi #merubah suatu nilai di dalam queue val
                if operasi == 0: #Jika waktu program habis, urutan program akan dikeluarkan
                    out = dequeue(key)
                    dequeue(val)
                    print("Iterasi ke-{} :\n Proses {} telah selesai diproses".format(num_iter,out))
                    print(" Data proses yang tersisa :\n Data : {}\n Waktu : {}\n".format(key,val))
                else: #Jika masih tersisa akan memasuki antrian lagi
                    enqueue(key,dequeue(key))
                    enqueue(val,dequeue(val))
                    print("Iterasi ke-{} :\n Proses {} sedang diproses dan sisa waktu proses {} = {}".format(num_iter,obj,obj,operasi))
                    print(" Data proses yang tersisa :\n Data : {}\n Waktu : {}\n".format(key,val))
            else: #jika nilai di dalam queue tidak memenuhi time proses dan disini urutan akan dikeluarkan dari proses karna waktu tersis habis
                operasi = val[0] - val[0]
                out = dequeue(key) #refer to program yg udh selesai
                dequeue(val)
                print("Iterasi ke-{} :\n Proses {} telah selesai diproses".format(num_iter,out))
                print(" Data proses yang tersisa :\n Data : {}\n Waktu : {}\n".format(key,val))
            num_iter += 1
    if size(key) == 0:
        print("Program Selesai")

proses()