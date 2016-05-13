import math
import re
import StopWord
from Statistic import Stat


def test(stat, path='', n_test=10):
    allCat = {'Crime and law': 0, 'Culture and entertainment': 0, 'Disasters and accidents': 0,
              'Science and technology': 0, 'Health': 0}
    callBack = dict(allCat)
    callAll = dict(allCat)
    stopWord = StopWord.getStopWord()
    termSum = len(stat.terms)
    correct = 0
    wrong = 0
    for n in range(1, n_test+1):
        filename = path + str(n) + '.txt'

        with open(filename, 'rb') as fin:
            title = fin.readline().strip()
            termList = re.split('[^a-zA-Z]+', fin.readline())
            maxi = 0
            toCat = ''

            for cat in stat.cats:   #
                noC = stat.cats[cat]
                p = 0.0
                for t in termList:
                    t = t.lower()
                    if not (t in stopWord or len(t) == 1):
                        if t in stat.terms:
                            noT = stat.termToInt[t]
                            p += math.log(1.0 * (stat.termInCat[noC][noT] + 1) / (stat.catTermAmount[noC] + termSum))
                p += math.log(1.0 * (stat.catTermAmount[noC] + 0.01) / stat.totalTerm)
                if p > maxi or toCat == '':
                    maxi = p
                    toCat = cat

            cat = fin.readline().strip()
            if cat in stat.cats:
                allCat[cat] += 1
                callAll[toCat] += 1
                if toCat == cat:
                    callBack[cat] += 1
                    correct += 1
                    print(title + '  :  ' + cat + '   toCat: ' + toCat + '  Yes')
                else:
                    wrong += 1
                    print(title + '  :  ' + cat + '   toCat: ' + toCat + '  No')

    print('\nTotal Precision:  correct / total = %d / %d' % (correct, correct + wrong))
    for cat in allCat:
        print('[' + cat + ']')
        if callAll[cat] > 0:
            p = callBack[cat] * 100.0 / callAll[cat]
        else:
            p = -1
        if allCat[cat] > 0:
            r = callBack[cat] * 100.0 / allCat[cat]
        else:
            r = -1
        print('Precision : %d / %d = %.3f%%' % (callBack[cat], callAll[cat], p))
        print('Recall : %d / %d = %.3f%%' % (callBack[cat], allCat[cat], r))
        print('F = %.3f%%' % (2.0 * p * r / (p + r)))

# stat = Stat()
# with open('log/log.txt','rb') as f:
#     stat.totalCat = int(f.readline().strip())
#     stat.cats = dict(f.readline().strip())
#     stat.totalTerm = int(f.readline().strip())
#     stat.terms = list(f.readline().strip())
#     stat.termToInt = dict(f.readline().strip())
#     stat.termAmount = list(f.readline().strip())
#     stat.termInDoc = list(f.readline().strip())
#     stat.catTermAmount = list(f.readline().strip())
#     stat.termInCat = list(f.readline().strip())

# print(stat.termInCat)
