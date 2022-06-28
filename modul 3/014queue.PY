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