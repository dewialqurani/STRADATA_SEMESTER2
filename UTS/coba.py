def createDeque():
    q = []
    return q
def addFront(q,data):
    q.insert(0,data)
    return(q)
def addRear(q,data):
    q.append(data)
    return(q)
def removeRear(q):
    data=q.pop
    return(data)
def removeFront(q):
    data=q.pop(0)
    return(data)
def isEmpty(q):
    return(d==[])
def size(q):
    return (len(q))

def any(p):
    deq=createDeque()
    for q in p:
        addF ront(deq,q)
    hasil=0
    while size(deq)>1:
        if removeFront(deq)==removeRear(deq):
            hasil+=1
        return hasil
print(any('hannah'),any('2002'),any('deques'))