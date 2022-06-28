def createdeque():
    d=[]
    return(d)
def addfront(d,data):
    d.insert(0,data)
    return(d)
def addrear(d, data):
    d.append(data)
    return(d)
def removerear(d):
    data=d.pop()
    return(data)
def removefront(d):
    data=d.pop(0)
    return(data)
def isEmpty(d):
    return(d==[])
def size(d):
    return(len(d))

def tower(n,asal,bantuan,tujuan):
    if n==1:
        print('\n')
        print('Lempengan - 1 dari - ', asal,'ke - ',tujuan)
        if asal=='A' and tujuan=='B':
            addfront(B1,removefront(A1))
        elif asal=='B' and tujuan=='C':
            addfront(C1,removefront(B1))
        elif asal=='C' and tujuan=='A':
            addfront(A1,removefront(C1))
        print('A = ')
        for i in A1:
            print('|',i,'|')
        print('B = ')
        for i in B1:
            print('|',i,'|')
        print('C = ')
        for i in C1:
            print('|',i,'|')


    else:
        tower(n-1,asal,tujuan,bantuan)
        print('\n')
        print('Lempengan - ',n, 'dari - ',asal,'ke - ', tujuan)
        if asal=='A' and tujuan=='C':
            addfront(C1,removefront(A1))
        elif asal=='A' and tujuan=='B':
            addfront(B1,removefront(A1))
        elif asal=='C' and tujuan=='B':
            addfront(B1,removefront(C1))
        elif asal=='B' and tujuan=='A':
            addfront(A1,removefront(B1))
        elif asal=='B' and tujuan=='C':
            addfront(C1,removefront(B1))
        print('A = ')
        for i in A1:
            print('|',i,'|')
        print('B = ')
        for i in B1:
            print('|',i,'|')
        print('C = ')
        for i in C1:
            print('|',i,'|')
        tower(n-1,bantuan,asal,tujuan)

print('Pemindahan 4 Lempengan dari A ke C dengan Menggunakan Bantuan B')
A1=createdeque()
B1=createdeque()
C1=createdeque()
addrear(A1,1)
addrear(A1,2)
addrear(A1,3)
addrear(A1,4)
tower(4,'A','B','C')