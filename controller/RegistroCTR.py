
from os import getcwd
from sys import path, platform
path.extend(['/'.join(getcwd().split('/')[0:-4])])

from model.DAO.RegistroDAO import RegistroDAO
from model.DMO.RegistroDMO import RegistroDMO


class RegistroCRT():

    def CadastrarRegistro(self,Laboratorio,NumeroPatri,NumeroSerie,Padrao,Modelo,Fabricante,
                        DataCali,DataChec,DataVenc,DataProxCali,DataSaida):

            registroDAO = RegistroDAO()

            registroDAO.Laboratorio = Laboratorio
            registroDAO.NumeroPatri = NumeroPatri
            registroDAO.NumeroSerie = NumeroSerie
            registroDAO.Padrao = Padrao
            registroDAO.Modelo = Modelo
            registroDAO.Fabricante = Fabricante
            registroDAO.DataCali = DataCali
            registroDAO.DataChec = DataChec
            registroDAO.DataVenc = DataVenc
            registroDAO.DataProxCali = DataProxCali
            registroDAO.DataSaida = DataSaida
        
            registroDMO = RegistroDMO()
            registroDMO.CadastrarRegistro(registroDAO)


def AtualizarRegistro(self,IDReg,Laboratorio,NumeroPatri,NumeroSerie,Padrao,Modelo,Fabricante,
                        DataCali,DataChec,DataVenc,DataProxCali,DataSaida):

            registroDAO = RegistroDAO()

            registroDAO.Laboratorio = Laboratorio
            registroDAO.NumeroPatri = NumeroPatri
            registroDAO.NumeroSerie = NumeroSerie
            registroDAO.Padrao = Padrao
            registroDAO.Modelo = Modelo
            registroDAO.Fabricante = Fabricante
            registroDAO.DataCali = DataCali
            registroDAO.DataChec = DataChec
            registroDAO.DataVenc = DataVenc
            registroDAO.DataProxCali = DataProxCali
            registroDAO.DataSaida = DataSaida
        
            registroDMO = RegistroDMO()
            registroDMO.CadastrarRegistro(IDReg,registroDAO)

def PesquisarTodosRegistro():
        registroDMO = RegistroDMO()
        query = registroDMO.PesquisarTodosRegistro()

        return query

def PesquisarRegistro(tipo, valor):
        registroDMO = registroDMO()
        query = registroDMO.PesquisarCliente(valor, tipo)

        return query

def ExcluirRegistro(IDReg):
        registroDMO = registroDMO()
        registroDMO.ExcluirCliente(IDReg)

'''

bla = RegistroCRT()
bla.CadastrarRegistro('UA30',
'7747453533',
'36961355552121',
'Osciloscópio',
'Fluke Sa20',
'Fluke',
'27/04/2020',
'20/04/2020',
'27/04/2021',
'27/04/2021',
'21/04/2021')
'''