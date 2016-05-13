import StopWord
import re
# what we need to know ?
# category proportion
# TF IDF term: frequency of each word ; how many documents include this word
# this term: how many doc include
# the amount of each term
# total amount of terms
# each cat have how many terms
# the amount of each term in each cat
# stopping-use word filter


def parse(stat, path='mirror/',  n_news=10000):
    stopWord = StopWord.getStopWord()
    print(str(stopWord))
    lastDoc = []
    for number in range(1, n_news+1):
        filename = path + str(number) + '.txt'
        with open(filename, 'rb') as fin:
            if fin:
                s = fin.readline()    # title
                print(number, s)
                s = fin.readline()    # body
                termList = re.split('[^a-zA-Z]+', s)
                pass
                s = fin.readline()    # category
                if s in stat.cats:
                    for item in termList:
                        item = item.lower()
                        if not ((item in stopWord) or (len(item) == 1)):
                            stat.catTermAmount[stat.cats[s]] += 1
                            if not (item in stat.terms):
                                stat.termToInt[item] = len(stat.terms)
                                stat.terms.append(item)
                                stat.termInDoc.append(0)
                                stat.termAmount.append(0)
                                lastDoc.append(-1)
                            stat.totalTerm += 1
                            no = stat.termToInt[item]
                            if lastDoc[no] != number:
                                lastDoc[no] = number
                                stat.termInDoc[no] += 1
                            stat.termAmount[no] += 1
                            stat.termInCat[stat.cats[s]][no] += 1
