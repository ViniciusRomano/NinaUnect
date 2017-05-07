
import psycopg2
import traceback
import time
from Permanencia import *
from Funcionario import *

class DB(object):


    def localCon(self):
        conn_string = "dbname= 'Teste_nina2' user= 'postgres'"
        print("Conectando ao banco de dados\n -> %s" % (conn_string))
        try:
            conn = psycopg2.connect(conn_string)
        except:
            traceback.print_exc()

        print("Conectado!\n")

        # criando um cursor para manipular o bd
        self.cur = conn.cursor()

    def __init__(self):
        try:
            self.conn = psycopg2.connect(
                database='d19e5ljbdi1afl',
                user='gbfwfvsmhymykz',
                password='b8d37cd6bf409ac1e8c3ee0ca6d3ca8ced763481fa040d728322412e37cd6352',
                host='ec2-50-17-207-16.compute-1.amazonaws.com',
                port=5432
            )
            self.cur = self.conn.cursor()
        except:
            traceback.print_exc()

    # criacao da tabela funcionario
    def createTableFuncionario(self):
        try:
            self.cur.execute('''CREATE TABLE IF NOT EXISTS Funcionario(
                    ra VARCHAR NOT NULL,
    				nome VARCHAR NOT NULL,
    				rfid VARCHAR,
    				constraint pkFuncionario primary key (ra)
    				);
    				''')

            self.conn.commit()
        except:
            traceback.print_exc()

    # ccriacao da tabela permanencia
    def createTablePermanencia(self):
        #  ra, data, hEntrada, hSaida
        try:
            self.cur.execute('''CREATE TABLE IF NOT EXISTS Permanencia(
                    id_permanencia SERIAL,
    				data DATE NOT NULL,
    				entrada TIME NOT NULL,
    				saida TIME NOT NULL,
    				ra VARCHAR NOT NULL, 
    				constraint pkPermanencia PRIMARY KEY (id_permanencia, ra),
    				constraint fkPermanenciaFuncionario FOREIGN KEY (ra) REFERENCES Funcionario (ra)
    				);''')

            self.conn.commit()
        except:
            traceback.print_exc()

    # inserindo dados na tabela permanencia
    def insertFuncionario(self, funcionario):
        # verificando se o ra tem 7 digitos
        #if len(str(funcionario.ra)) < 7:
        #    print("RA invalido")
        #    return -1
        # ainda nao se sabe como sera o rfid, inativo por enquanto
        # if len(RFID) < 10:
        #   print("RFID invalido")
        #    return -1
        try:
            self.cur.execute("INSERT INTO Funcionario (ra,rfid,nome) VALUES('{0}', '{1}', '{2}')"
                             .format(funcionario.ra, funcionario.rfid, funcionario.nome))
            self.conn.commit()
        except:
            traceback.print_exc()
            return 0

        return 1

    # inserindo dados na tabela permanencia
    def insertPermanencia(self, permanencia):
        #if len(str(permanencia.ra)) < 7:
        #    print("RA invalido")
        #    return -1
        try:

            self.cur.execute(
                "INSERT INTO Permanencia (ra, data, entrada, saida) VALUES('{0}', '{1}', '{2}', '{3}')"
                    .format(permanencia.ra, permanencia.data, permanencia.hEntrada, permanencia.hSaida))
            self.conn.commit()
        except:
            traceback.print_exc()
            return 0
        return 1


    # update na tabela Funcionario
    def updateFuncionario(self, oldFuncionario, newFuncionario):
        try:
            self.cur.execute(
                "UPDATE Funcionario SET ra = '{0}', nome = '{1}', rfid = '{2}' WHERE ra = '{3}'"
                    .format(newFuncionario.ra, newFuncionario.nome, newFuncionario.rfid, oldFuncionario.ra))
            self.conn.commit()
        except:
            traceback.print_exc()
            return 0
        return 1

    # update na tabela Permanencia
    def updatePermanencia(self, oldPermanencia, newPermanencia):
        try:
            self.cur.execute(
                "UPDATE Funcionario SET ra = '{0}', data = '{1}', entrada = '{2}', saida = '{3}',  WHERE ra = '{4}'"
                    .format(newPermanencia.ra, newPermanencia.data, newPermanencia.entrada, newPermanencia.saida, oldPermanencia.ra))
            self.conn.commit()
        except:
            traceback.print_exc()
            return 0
        return 1

    # dando update em um valor da coluna RFID
    def updateRFID(self, oldValue, newValue):
        self.cur.execute(
            "UPDATE Funcionario SET rfid = %s WHERE rfid = '%s'", (newValue, oldValue))
        self.conn.commit()


    # resgatando dados da tabela Funcionario
    def selectListaFuncionario(self):
        try:
            self.cur.execute("SELECT ra, nome, rfid from Funcionario")
            rows = self.cur.fetchall()
            listaF = []
            for row in rows:
                f = Funcionario(row[0], row[1], row[2])
                listaF.append(f)
        except:
            traceback.print_exc()
            return 0

        return listaF

    # resgatando dado especifico da tabela Funcionario, chave de select: RA
    def selectFuncionario(self, ra):
        try:
            self.cur.execute("SELECT ra, nome, rfid from Funcionario WHERE ra = '{0}'" .format(ra))
            rows = self.cur.fetchall()

            if len(rows) == 1:
                f = Funcionario(rows[0][0], rows[0][1], rows[0][2])
                return f
            else:
                return None

        except:
            traceback.print_exc()
            return 0


    # regatando dados da tabela Permanencia
    def selectListaPermanencia(self):
        try:
            self.cur.execute("SELECT ra, data, entrada, saida from Permanencia")
            rows = self.cur.fetchall()
            listaP = []
            for row in rows:
                p = Permanencia(row[0], row[1], row[2], rows[3], 'OK', '')
                listaP.append(p)
        except:
            traceback.print_exc()
            return 0

        return listaP

    # resgatando dado especifico da tabela Permanencia, chave de select: RA
    def selectPermanencia(self, ra):
        try:
            self.cur.execute("SELECT ra, data, entrada, saida from Permanencia WHERE ra = '{0}'" .format(ra))
            rows = self.cur.fetchall()

            if len(rows) == 1:
                p = Permanencia(rows[0][0], rows[0][1], rows[0][2], rows[0][3], 'OK', '')
                return p
            else:
                return None

        except:
            traceback.print_exc()
            return 0

    # drop table caso necessario
    #def dropAllTables(self):
    #    try:
    #       self.cur.execute("DROP table Permanencia")
    #       self.cur.execute("DROP table Funcionario")
    #    except:
    #        traceback.print_exc()
    #    print("TABLES DROPPED")




