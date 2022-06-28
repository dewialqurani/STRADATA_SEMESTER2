#fungsi-fungsi yang digunakan  untuk menerapkan fungsi stack
def stack() :
    s=[]
    return s
def push (s,data) : #push untuk penambahan data
    s.append(data)
    return s
def pop (s) :   #pop untuk menghapus data
    data = s.pop()
    return data
def peek(s) :   #peek informasi data yang terletak pada posisi top 
    return (s[len(s)-1])
def isEmpty(s) :    #isEmpty memeriksa apakah stack dalam keadaan kosong
    return(s==[])
def size (s) :  #jumlah data atau ukuran yang terdapat pada stack
    return(len(s))
def size(s):
    return(len(s))

st=stack()
push(st,5)
push(st,8)
push(st,peek(st))
pop(st)
print(st)