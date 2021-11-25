import sqlite3
import PySimpleGUI as sg
from os import close
from datetime import date
from datetime import datetime

escolha = ""
tema = ""

#if escolha == "Claro":
#    tema = "TealMono"
#if escolha == "Escuro":
#    tema = "DarkBlack"


conection = sqlite3.connect('bd.db')

c = conection.cursor()

# Cria tabela alunos


def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS alunos(id INTEGER PRIMARY KEY AUTOINCREMENT, nomec text, sexo text, altura real, datan text, peso real, imc real, status real)')


# create_table()

# Cria tabela personal
def create_table_personal():
    c.execute('CREATE TABLE IF NOT EXISTS personal(id INTEGER PRIMARY KEY AUTOINCREMENT, nomep text, sexo text, altura real, datan text, peso real, status real)')

# create_table_personal()


def create_table_adm():
    c.execute('CREATE TABLE IF NOT EXISTS admin(id INTEGER PRIMARY KEY AUTOINCREMENT, nomeadm text, user text, passs int, passss int)')

# create_table_adm()


def create_table_plano():
    c.execute('CREATE TABLE IF NOT EXISTS planos(id INTEGER PRIMARY KEY AUTOINCREMENT, nomeplano text, codplano text)')

# create_table_plano()


def delete():
    c = conection.cursor()
    c.execute('DELETE * FROM alunos WHERE nomec = "Ativo"')
    dados_lidos = c.fetchall()
    conection.commit()

    for i in range(0, len(dados_lidos)):
        for j in range(0):
            # print(dados_lidos[i],[j])
            #print("")
            pass
# delete()


f_status = "%"
f_sexo = "%"
f_imcm = 0
f_imc = 1000
b_plano = "Z"
b_personal = "PEDRO"

# consulta com filtros


def listacrit_filtros(f_status, f_sexo, f_imcm, f_imc, b_plano, b_personal):
    c = conection.cursor()
    c.execute('SELECT * FROM alunos WHERE status like ? AND sexo like ? AND imc >= ? AND imc <= ? AND plano like ? AND nomep like ? ORDER BY nomec',
              (f_status, f_sexo, f_imcm, f_imc, b_plano, b_personal,))
    dadoslidos = c.fetchall()
    conection.commit()
    # print(dadoslidos)
    return dadoslidos
#listacrit_filtros(f_status, f_sexo,f_imcm,f_imc,b_plano,b_personal)


# lista alunos por criterios ativos ou inativos
def listacrit(crit):
    c = conection.cursor()
    c.execute('SELECT * FROM alunos WHERE status = ? ORDER BY nomec', (crit,))
    dadoslidos = c.fetchall()
    conection.commit()
    # print(dadoslidos)
    return dadoslidos


# lista plano por criterios ativos ou inativos
def listacritplano(critplano):
    c = conection.cursor()
    c.execute(
        'SELECT * FROM planos WHERE statusplano = ? ORDER BY nomeplano', (critplano,))
    dadoslidosplano = c.fetchall()
    conection.commit()
    # print(dadoslidos)
    return dadoslidosplano

# lista personal por criterios ativos ou inativos


def listacritpersonal(critpersonal):
    c = conection.cursor()
    c.execute(
        'SELECT * FROM personal WHERE status = ? ORDER BY nomep', (critpersonal,))
    dadoslidospersonal = c.fetchall()
    conection.commit()
    # print(dadoslidos)
    return dadoslidospersonal


def pesquisa(pesquisa3):
    c = conection.cursor()
    #c.execute('SELECT * FROM alunos WHERE status = ? ORDER BY nomec', (crit,))
    c.execute('select * from alunos where nomec like ? ORDER BY nomec',
              (pesquisa3,) or (""))
    dados_lidos = c.fetchall()
    conection.commit()
    # print(dados_lidos)

    return dados_lidos
    # select * from usuarios where nomes like '%pedro%'
    

# Pesquisa planos


def pesquisaplano():
    c = conection.cursor()

    c.execute('select * from planos')
    dados_lidosplano = c.fetchall()
    conection.commit()
    # print(dados_lidosplano)

    return dados_lidosplano
    # select * from usuarios where nomes like '%pedro%'


# pesquisaplano()

# lista personal
def pesquisapersonal():
    c = conection.cursor()

    c.execute('select * from personal')
    dados_lidospersonal = c.fetchall()
    conection.commit()
    # print(dados_lidosplano)

    return dados_lidospersonal
    # select * from usuarios where nomes like '%pedro%'


# pesquisaplano()


# 3

def lista():
    c = conection.cursor()
    c.execute('SELECT * FROM alunos ORDER BY nomec ')
    dadoslidos = c.fetchall()
    conection.commit()
    # print(dadoslidos)
    return dadoslidos


def deletesel(x):
    c.execute('DELETE FROM alunos WHERE datem = ?', (x,))
    conection.commit()


# delete plano
def deleteselplano(x):
    c.execute('DELETE FROM planos WHERE nomeplano = ?', (x,))
    conection.commit()

# delete personal
def deleteselpersonal(x):
    c.execute('DELETE FROM personal WHERE nomep = ?', (x,))
    conection.commit()    


# Updade
nv = "ad"
cond = "FREDY ROMANO"


def upl(nv, cond):
    conection = sqlite3.connect('bd.db')
    c = conection.cursor()

    c.execute('UPDATE alunos SET status = ? WHERE nomec =?', (nv, cond))
    conection.commit()

# upl(nv,cond)


# Updade NOVO
dm = "26/09/2021 10:34:27"
a = 65
p = 90
st = "novo"
n = "ALICIA"
im = 0
pl = "ALICIA"
pers = "44444444444"


def upl_novo(a, p, st, im, pl, pers, dm):
    conection = sqlite3.connect('bd.db')
    c = conection.cursor()

    c.execute('UPDATE alunos SET altura = ?, peso =?, status =?,imc =?,plano =?,nomep =? WHERE datem =?',
              (a, p, st, im, pl, pers, dm))
    conection.commit()


# update cadastro plano
def upl_novoplano(stp, n):
    conection = sqlite3.connect('bd.db')
    c = conection.cursor()

    c.execute('UPDATE planos SET statusplano = ? WHERE nomeplano =?', (stp, n))
    conection.commit()

# update cadastro personal


def upl_novopersonal(at, ps, stp, n):
    conection = sqlite3.connect('bd.db')
    c = conection.cursor()

    c.execute(
        'UPDATE personal SET altura =?, peso =?, status = ? WHERE nomep =?', (at, ps, stp, n))
    conection.commit()


# cadastro de alunos
nomec = "ssa"
cpf=""
datem = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
sexo = "sasas"
altura = 1
datan = "06/08/80"
peso = 80
imc = 5
status = "sdsd"
plano = "planoaqqqqq"
nomep = ""


def cadastrardados(nomec, cpf,datem, sexo, altura, datan, peso, imc, status, plano, nomep):
    conection = sqlite3.connect('bd.db')
    c = conection.cursor()
    c.execute('INSERT INTO alunos (nomec, cpf,datem, sexo, altura,  datan, peso, imc, status, plano, nomep) VALUES (?,?,?,?,?,?,?,?,?,?,?)',
              (nomec, cpf, datem, sexo, altura,  datan, peso, imc, status, plano, nomep))
    conection.commit()
#cadastrardados(nomec,datem,sexo, altura,  datan, peso ,imc, status,plano)


def cadastrardados_h(nomec, cpf, datem, sexo, altura, datan, peso, imc, status, plano, nomep):
    conection = sqlite3.connect('bd.db')
    c = conection.cursor()
    c.execute('INSERT INTO h_alunos (nomec, cpf, datem, sexo, altura,  datan, peso, imc, status, plano,nomep) VALUES (?,?,?,?,?,?,?,?,?,?,?)',
              (nomec, cpf,datem, sexo, altura,  datan, peso, imc, status, plano, nomep))
    conection.commit()

#cadastrardados_h(nomec,datem,sexo, altura,  datan, peso ,imc, status,plano,nomep)

# cadastro de personall


def cadastrardados_personal(nomep, sexo, altura,  datan, peso, status):
    conection = sqlite3.connect('bd.db')
    c = conection.cursor()
    c.execute('INSERT INTO personal (nomep, sexo, altura,  datan, peso, status) VALUES (?,?,?,?,?,?)',
              (nomep, sexo, altura,  datan, peso, status))
    conection.commit()

# cadastro de usuario


def cadastraruser(nomeadm, user, passs, passss, previlegio):
    conection = sqlite3.connect('bd.db')
    c = conection.cursor()
    c.execute('INSERT INTO admin (nomeadm, user, passs, passss,previlegio) VALUES (?,?,?,?,?)',
              (nomeadm, user, passs, passss, previlegio))
    conection.commit()

 # cadastro de planos


def cadastrarplanos(nomeplano, codplano, statusplano):
    conection = sqlite3.connect('bd.db')
    c = conection.cursor()
    c.execute('INSERT INTO planos (nomeplano, codplano,statusplano) VALUES (?,?,?)',
              (nomeplano, codplano, statusplano))
    conection.commit()


def listaplano():
    c = conection.cursor()
    c.execute('SELECT codplano FROM planos WHERE statusplano ="ATIVO" ')
    dadoslidos = c.fetchall()
    conection.commit()
    #print(dadoslidos)
    return dadoslidos
# listaplano()


def listapersonal():
    c = conection.cursor()
    c.execute('SELECT nomep FROM personal ORDER BY nomep')
    dadoslidos = c.fetchall()
    conection.commit()
    #print(dadoslidos)    
    return dadoslidos
listapersonal()

# conta registros com filtros


def listacrit_filtros_qtd(f_status, f_sexo, f_imcm, f_imc, b_plano, b_personal):
    c = conection.cursor()
    c.execute('select count(nomec) from alunos WHERE status like ? AND sexo like ? AND imc >= ? AND imc <= ? AND plano like ? AND nomep like ? ORDER BY nomec',
              (f_status, f_sexo, f_imcm, f_imc, b_plano, b_personal,))
    dadoslidos = c.fetchall()
    conection.commit()
    # print(dadoslidos)
    return dadoslidos
#listacrit_filtros_qtd(f_status, f_sexo,f_imcm,f_imc,b_plano,b_personal)


# select count(nomec) from alunos
usuario = "EUDSON"


def retlogin(logado):
    c = conection.cursor()
    c.execute('SELECT previlegio FROM admin WHERE user =?', (logado,))
    dadoslidos = c.fetchall()
    conection.commit()
    #print(dadoslidos)
    return dadoslidos

# retlogin(usuario)

cpf_retornado = "00938936476"
#Lista todos cpf
def lista_cpf(cpf_digitado):
    c = conection.cursor()
    c.execute('select cpf from alunos where cpf like ? ORDER BY cpf',
              (cpf_digitado,))
    cpf_retornado = c.fetchall()
    conection.commit()
    #print(cpf_retornado)

    return cpf_retornado 
lista_cpf(cpf_retornado) 


