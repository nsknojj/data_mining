# what we need to know ?
# category proportion
# TF IDF term: frequency of each word ; how many documents include this word
# this term: how many doc include
# the amount of each term
# total amount of terms
# each cat have how many terms
# the amount of each term in each cat
# stopping-use word filter
import Input
import Test
from Statistic import Stat


stat = Stat()
Input.parse(stat, path='train/', n_news=6400)  # 6727
# with open('log/log.txt','wb') as f:
#     f.write(str(stat.totalCat) + '\n')
#     f.write(str(stat.cats) + '\n')
#     f.write(str(stat.totalTerm) + '\n')
#     f.write(str(stat.terms) + '\n')
#     f.write(str(stat.termToInt) + '\n')
#     f.write(str(stat.termAmount) + '\n')
#     f.write(str(stat.termInDoc) + '\n')
#     f.write(str(stat.catTermAmount) + '\n')
#     f.write(str(stat.termInCat) + '\n')
Test.test(stat, path='test/', n_test=1600)
# print stat.terms
# print stat.termInDoc
