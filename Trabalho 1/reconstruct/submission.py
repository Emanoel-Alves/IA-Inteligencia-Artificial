import shell
import util
import wordsegUtil

############################################################
# Problema 1: Segmentacao de Palavras com funcao de custo 'unigram'

class SegmentationProblem(util.SearchProblem):
    def __init__(self, query, unigramCost):
        self.query = query
        self.unigramCost = unigramCost

    def startState(self):
        return self.query
        # (Estado inicial e o inicio da palavra na qual e a query)

    def isEnd(self, state):
        return state == ''
        # (O estado final e quando chegar no fim da entrada passada)

    def succAndCost(self, state):
        possible = []
        stateSize = len(state)+1
        for i in range(stateSize): 
            possible.append((state[0:i], state[i:], self.unigramCost(state[0:i])))
        return possible
        # (Possible e uma lista que possui triplas, na qual as triplas (palavra, o restante da entrada, o custo da palavra que foi encontrada))

def segmentWords(query, unigramCost):
    if len(query) == 0:
        return ''

    ucs = util.UniformCostSearch(verbose=0)
    ucs.solve(SegmentationProblem(query, unigramCost))

    # (Retorna a juncao das palavras guarda em acoes, caso tenha alguma palavra)
    if ( len(ucs.actions) > 0 ): return ' '.join(ucs.actions)
    else: return query

############################################################
# Problema 2: Insercao de Vogais com custo 'bigram'

class VowelInsertionProblem(util.SearchProblem):
    def __init__(self, queryWords, bigramCost, possibleFills):
        self.queryWords = queryWords
        self.bigramCost = bigramCost
        self.possibleFills = possibleFills

    def startState(self):
        # BEGIN_YOUR_CODE (solucao em 1 linha de codigo, mas utilize quantas linhas julgar necessario)
        raise Exception("Not implemented yet")
        # END_YOUR_CODE

    def isEnd(self, state):
        # BEGIN_YOUR_CODE (solucao em 2 linhas de codigo, mas utilize quantas linhas julgar necessario)
        raise Exception("Not implemented yet")
        # END_YOUR_CODE

    def succAndCost(self, state):
        # BEGIN_YOUR_CODE (solucao em 8 linhas de codigo, mas utilize quantas linhas julgar necessario)
        raise Exception("Not implemented yet")
        # END_YOUR_CODE

def insertVowels(queryWords, bigramCost, possibleFills):
    # BEGIN_YOUR_CODE (solucao em 3 linhas de codigo, mas utilize quantas linhas julgar necessario)
    raise Exception("Not implemented yet")
    # END_YOUR_CODE

############################################################
# Problema 3: Programa Integrado com custo 'bigram'

class JointSegmentationInsertionProblem(util.SearchProblem):
    def __init__(self, query, bigramCost, possibleFills):
        self.query = query
        self.bigramCost = bigramCost
        self.possibleFills = possibleFills

    def startState(self):
        # BEGIN_YOUR_CODE (solucao em 1 linha de codigo, mas utilize quantas linhas julgar necessario)
        raise Exception("Not implemented yet")
        # END_YOUR_CODE

    def isEnd(self, state):
        # BEGIN_YOUR_CODE (solucao em 2 linhas de codigo, mas utilize quantas linhas julgar necessario)
        raise Exception("Not implemented yet")
        # END_YOUR_CODE

    def succAndCost(self, state):
        # BEGIN_YOUR_CODE (solucao em 14 linhas de codigo, mas utilize quantas linhas julgar necessario)
        raise Exception("Not implemented yet")
        # END_YOUR_CODE

def segmentAndInsert(query, bigramCost, possibleFills):
    if len(query) == 0:
        return ''

    # BEGIN_YOUR_CODE (solucao em 4 linhas de codigo, mas utilize quantas linhas julgar necessario)
    raise Exception("Not implemented yet")
    # END_YOUR_CODE

############################################################

if __name__ == '__main__':
    shell.main()
