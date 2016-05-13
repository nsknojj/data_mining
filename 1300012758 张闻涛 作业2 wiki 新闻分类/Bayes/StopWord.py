def getStopWord():
    l = []
    with open('stopword.txt', 'r') as f:
        for x in f.readlines():
            l.append(x.strip())
    return l
