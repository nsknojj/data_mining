class Stat(object):
    totalCat = 5
    cats = {'Crime and law': 0, 'Culture and entertainment': 1,
            'Disasters and accidents': 2, 'Science and technology': 3, 'Health': 4}
    totalTerm = 0
    terms = []  # term list
    termToInt = {}  # term dict
    termAmount = []  # each term's amount
    termInDoc = []  # how many documents include this term
    catTermAmount = [0 for col in range(5)]  # each cat have how many terms
    termInCat = [[0 for col in range(80000)] for row in range(5)]  # amount of each term in each cat
