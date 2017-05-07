from bd_nina import *
from Funcionario import *
from Permanencia import *
import codecs

class manutencaoBD(object):

    def __init__(self):
        self.bd = DB()

    def inserirFuncArquivo(self, path):
        arq = codecs.open(path, 'r', encoding='utf-8')
        for line in arq:
            s = line.split('\t')
            print(s[0]+'-'+s[1])
            f = Funcionario(s[0], s[1], '')
            self.bd.insertFuncionario(f)



if __name__ == '__main__':
    a = manutencaoBD()
    #a.bd.dropAllTables()
    #a.bd.createTableFuncionario()
    #a.bd.createTablePermanencia()
    #a.inserirFuncArquivo('Book1.txt')
    #a.bd.insertFuncionario(Funcionario('1234567', '', 'TESTE'))
    print(a.bd.selectPermanencia(Permanencia('1234567', '', '', '', '', '')).ra)

