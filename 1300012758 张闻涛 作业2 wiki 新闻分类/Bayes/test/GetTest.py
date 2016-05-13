tot = {'Crime and law': 540, 'Culture and entertainment': 300,
            'Disasters and accidents': 320, 'Science and technology': 320, 'Health': 120}
totalNum = {'Crime and law': 0, 'Culture and entertainment': 0,
       'Disasters and accidents': 0, 'Science and technology': 0, 'Health': 0}
ct = 0
train = 0
for i in range(1, 8705):
    infile = '../mirror/' + str(i) + '.txt'
    with open(infile, 'rb') as fin:
        if fin:
            title = fin.readline()
            body = fin.readline()
            cat = fin.readline().strip()
            if cat in tot:
                totalNum[cat] += 1
                if tot[cat] > 0:
                    tot[cat] -= 1
                    ct += 1
                    with open(str(ct) + '.txt', 'wb') as fout:
                        fout.write(title)
                        fout.write(body)
                        fout.write(cat)
                else:
                    train += 1
                    with open('../train/' + str(train) + '.txt', 'wb') as fout:
                        fout.write(title)
                        fout.write(body)
                        fout.write(cat)

print(tot)
print(totalNum)
