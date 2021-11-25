from datetime import datetime
from datetime import date
import time
import bd
from os import close, replace
import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import Button, _refresh_debugger
import TelasCadastros as tc
import TelasConsulta as tcs
import TelasMenu as tm
import TelasPopup as tp
import TelasUpgrade as tu
from validate_docbr import CPF
cpf = CPF()


# VARIAVES JANELAS
janela1 = tm.janela_login()
janela2 = None
janela3 = None
janela4 = None
janela5 = None


# FUNÇÕES LIMPA CAMPOS
def limpaadm():
    window.find_element('senha').Update('')
    window.find_element('nome').Update('')


def limpacampos():
    window.find_element('nomec').Update('')
    window.find_element('altura').Update('')
    window.find_element('peso').Update('')
    window.find_element('datan').Update('')
    window.find_element('sexo').Update('')


def limpacampospersonal():

    window.find_element('nomep').Update('')
    window.find_element('altura').Update('')
    window.find_element('peso').Update('')
    window.find_element('datan').Update('')
    window.find_element('sexo').Update('')


def limpacampospersonal2():
    tc.nomec = ""
    tc.sexo = ""
    tc.altura = ""
    tc.datan = ""
    # t.datem = ""
    tc.peso = ""
    tc.status = ""


def limpaadmcad():
    window.find_element('nomeadm').Update('')
    window.find_element('user').Update('')
    window.find_element('passs').Update('')
    window.find_element('passss').Update('')


def limpaadmsenha():
    window.find_element('passs').Update('')
    window.find_element('passss').Update('')


def limpaplano():
    window.find_element('nomeplano').Update('')
    window.find_element('codplano').Update('')

# Funções


# Loop telas
while True:
    window, eventos, valores = sg.read_all_windows()
    if window == janela1 and eventos == sg.WIN_CLOSED:
        janela1.close()
        break
    if window == janela2 and eventos == sg.WIN_CLOSED:
        janela2.close()
        break
    if window == janela3 and eventos == sg.WIN_CLOSED:
        janela3.close()

    if window == janela4 and eventos == sg.WIN_CLOSED:
        janela4.close()

    if window == janela1 and eventos == '  Sair  ':
        janela1.close()
        break

    if window == janela2 and eventos == 'ok_conf_cad':
        janela2.close()
        # break

    if window == janela2 and eventos == '  Sair  ':
        janela2.close()
    if window == janela3 and eventos == '  Sair  ':
        janela3.close()
    if window == janela4 and eventos == 'popup_ok_cadasto':
        janela4.close()
        janela3.close()

    if window == janela4 and eventos == 'ok_conf_cad':
        janela4.close()

    if window == janela5 and eventos == 'ok_conf_cad':
        janela5.close()

    if window == janela1 and eventos == sg.WIN_CLOSED:
        janela1.close()

    # TELA LOGIN - ENTRAR
    if window == janela1 and eventos == 'Entrar':
        dadoslidos = bd.retlogin(valores['nome'])
        statement = f"SELECT user from admin WHERE user='{valores['nome']}' AND passs = '{valores['senha']}';"
        bd.c.execute(statement)
        if not bd.c.fetchone():
            #print("Login failed")
            limpaadm()
            tp.msg = "Dados não conferem, favor tentar novamente"
            janela2 = tp.janela_popup()

        else:
            #print("usurario", valores['nome'])
            #print("dadoslidos", dadoslidos[0][0])
            if dadoslidos[0][0] == "Master":
                # print("Welcome")
                janela1.close()
                janela2 = tm.janelamenuadm()

            if dadoslidos[0][0] == "Escrita":
                # print("Welcome")
                janela1.close()
                janela2 = tm.janelamenuescrita()

            if dadoslidos[0][0] == "Leitura":
                # print("Welcome")
                janela1.close()
                janela2 = tm.janelamenueleitura()

    # Cadastro de aluno
    if window == janela2 and eventos == 'Aluno':
        tc.nomec = ""
        tc.cpf = ""
        tc.altura = ""
        tc.peso = ""
        tc.datan = ""
        tc.sexo = ["MASCULINO", "FEMENINO"]
        tc.status = ["ATIVO", "INATIVO"]
        tc.plano = bd.listaplano()

        tc.nomep = bd.listapersonal()
        janela3 = tc.janela_cadastro()

    if window == janela3 and eventos == 'cad_aluno':
        # limpacampos()

        st_cpf = cpf.validate(str(valores['cpf']))
        if valores['nomec'] == "" or valores['sexo'] == "" or valores['altura'] == "" or valores['datan'] == "" or valores['peso'] == "" or valores['status'] == "" or valores['plano'] == "" or valores['nomep'] == "":
            tp.msg = "Favor prencher todos os campos corretamente"
            janela4 = tp.janela_popup()
        elif st_cpf == False:
            new_cpf_one = cpf.generate()  # gera cpf valido
            window.find_element('cpf').Update(new_cpf_one)  # gera cpf valido
            tp.msg = "Favor colocar um cpf valido"
            janela4 = tp.janela_popup()

        else:

            if bd.lista_cpf(valores['cpf']) != []:
                tp.msg = "Ja tem um cadastro com esse CPF"
                janela4 = tp.janela_popup()
                new_cpf_one = cpf.generate()  # gera cpf valido
                window.find_element('cpf').Update(
                    new_cpf_one)  # gera cpf valid
            else:
                #ehNumero = False

                #while (ehNumero == False):
                    chute = valores['altura']

                    try:
                        int(chute)
                        ps = float(valores['peso'].replace(',', '.'))
                        al = float(valores['altura'].replace(',', '.'))
                        tt = ps / (al*al)
                        valores['imc'] = round(tt, 2)
                        valores['datem'] = tc.datem

                        bd.cadastrardados(valores['nomec'].upper(), valores['cpf'], valores['datem'], valores['sexo'].upper(
                        ), valores['altura'], valores['datan'], valores['peso'], valores['imc'], valores['status'].upper(), valores['plano'][0], valores['nomep'][0])
                        bd.cadastrardados_h(valores['nomec'].upper(), valores['cpf'], valores['datem'], valores['sexo'].upper(
                        ), valores['altura'], valores['datan'], valores['peso'], valores['imc'], valores['status'].upper(), valores['plano'][0], valores['nomep'][0])
                        limpacampos()
                        ehNumero = True
                        tp.msg = "Dados Cadastrados com sucesso"
                        janela4 = tp.janela_popup_ok_cadasto()
                        

                    except ValueError:
                        try:
                            float(chute)
                            ps = float(valores['peso'].replace(',', '.'))
                            al = float(valores['altura'].replace(',', '.'))
                            tt = ps / (al*al)
                            valores['imc'] = round(tt, 2)
                            valores['datem'] = tc.datem

                            bd.cadastrardados(valores['nomec'].upper(), valores['cpf'], valores['datem'], valores['sexo'].upper(
                            ), valores['altura'], valores['datan'], valores['peso'], valores['imc'], valores['status'].upper(), valores['plano'][0], valores['nomep'][0])
                            bd.cadastrardados_h(valores['nomec'].upper(), valores['cpf'], valores['datem'], valores['sexo'].upper(
                            ), valores['altura'], valores['datan'], valores['peso'], valores['imc'], valores['status'].upper(), valores['plano'][0], valores['nomep'][0])
                            limpacampos()
                            ehNumero = True
                            tp.msg = "Dados Cadastrados com sucesso"
                            janela4 = tp.janela_popup_ok_cadasto()
                            

                        except ValueError:
                            print("digite altura valida")
                            tp.msg = "Favor peso e altura validos"
                            janela4 = tp.janela_popup()
  ##############################################################################################

    if eventos == 'data':
        janela4 = sg.popup_get_date(start_year=1980, month_names=[
                                    "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Junho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"])
        if janela4:
            month, day, year = janela4
            window['datan'].update(f"{day:0>2d}/{month:0>2d}/{year}")

    # CHAMA CADASTRO PERSONAL
    if window == janela2 and eventos == 'Personal':
        janela3 = tc.janela_cadastro_personal()

    if window == janela3 and eventos == 'cad_personal':

        if valores['nomep'] == "" or valores['sexo'] == "" or valores['altura'] == "" or valores['datan'] == "" or valores['peso'] == "" or valores['status'] == "":
            tp.msg = "Favor prencher todos os campos"
            janela4 = tp.janela_popup()
        else:
            bd.cadastrardados_personal(valores['nomep'].upper().replace(" ", "_"), valores['sexo'].upper(
            ), valores['altura'].upper(), valores['datan'], valores['peso'], valores['status'].upper())
            limpacampospersonal()
            tp.msg = "Dados Cadastrados com sucesso"
            janela4 = tp.janela_popup_ok_cadasto()

    # CHAMA CADASTRO ADM
    if window == janela2 and eventos == 'Cadastro User':
        janela3 = tc.janela_cad_admin()
    if window == janela3 and eventos == 'Cadastrarr':
        if valores['nomeadm'] == "" or valores['user'] == "" or valores['passs'] == "" or valores['passss'] == "" or valores['previlegio'] == "":
            tp.msg = "Favor prencher todos os campos"
            janela4 = tp.janela_popup()
        else:
            if valores['passs'] == valores['passss']:
                bd.cadastraruser(valores['nomeadm'].upper(
                ), valores['user'].upper(), valores['passs'], valores['passss'], valores['previlegio'])
                limpaadmcad()
                tp.msg = "Dados Cadastrados com sucesso"
                janela4 = tp.janela_popup_ok_cadasto()
            else:
                limpaadmsenha()
                tp.msg = "Senhas diferentes"
                janela4 = tp.janela_popup()
                # daqui acimi funciona

    # CHAMA MENU PLANO
    if window == janela2 and eventos == 'Plano':
        janela3 = tc.janela_cad_plano()

    if window == janela3 and eventos == 'Cadastrarrr':
        if valores['nomeplano'] == "" or valores['codplano'] == "":
            tp.msg = "Favor prencher todos os campos"
            janela4 = tp.janela_popup()
        else:
            bd.cadastrarplanos(
                valores['nomeplano'].upper(), valores['codplano'].upper().replace(" ", "_"), valores['statusplano'].upper())
            limpaplano()
            tp.msg = "Dados Cadastrados com sucesso"
            janela4 = tp.janela_popup()

            # daqui acimi funciona

    # CHAMA MENU ATUALZAÇÕES alunos
    if window == janela2 and eventos == 'Alunos':
        tu.plano = bd.listaplano()
        tu.nomep = bd.listapersonal()
        tu.plano.append("TODOS")
        tu.nomep.append("TODOS")
        tu.ret_plano = tu.plano
        tu.ret_personal = tu.nomep
        janela3 = tu.ativos()
        tu.i = 0
        listado = False
        #print("ao arbri janela",listado)

    # CHAMA MENU CONSULTA alunos
    if window == janela2 and eventos == 'Consulta Alunos':
        tcs.plano = bd.listaplano()
        tcs.nomep = bd.listapersonal()
        tcs.plano.append("TODOS")
        tcs.nomep.append("TODOS")
        tcs.ret_plano = tcs.plano
        tcs.ret_personal = tcs.nomep
        janela3 = tcs.consulta()
        tm.i = 0
        # LISTA TODOS ALUNOS
    if window == janela3 and eventos == 'listardados':
        listado = True
        # print(listado)
        dados_lidos = bd.lista()
        window.find_element('lido').Update(dados_lidos)
        row_colors = ((0, 'white'))
        ev = eventos

        # LISTA ALUNOS ATIVOS
    if window == janela3 and eventos == 'ativos':
        listado = True
        crit = "ATIVO"
        dados_lidos = bd.listacrit(crit)
        window.find_element('lido').Update(dados_lidos)
        ev = eventos

        # LISTA ALUNOS INATIVOS
    if window == janela3 and eventos == 'inativos':  # lista alunos inativos
        listado = True
        crit = "INATIVO"
        dados_lidos = bd.listacrit(crit)
        window.find_element('lido').Update(dados_lidos)
        ev = eventos

    # DELETA DADOS alunos
    if window == janela3 and eventos == 'delete':  # deleta selecionado

        if listado == False:
            tp.msg = "Favor Lista e depois selecionar um Alunoa ser deletado!"
            janela4 = tp.janela_popup_ok(tp.msg)
            #print("ao fechar",listado)
        else:
            ld = valores['lido']
            soma = sum(ld)
            x = dados_lidos
            y = x[soma][1]
            tu.a_peso = y
            tp.msg = "Confirmar a exclusão do aluno "+x[soma][2]
            janela4 = tp.janela_popup_del(tp.msg)

    if window == janela4 and eventos == 'SIM':
        bd.deletesel(y)
        window = janela3
        bd.lista()
        dados_lidos = bd.lista()
        window.find_element('lido').Update(dados_lidos)
        janela4.close()
        window.find_element('lido').Update(dados_lidos)
    if window == janela4 and eventos == 'NÃO':
        janela4.close()

    # Alterar cadastro de alunos
    if window == janela3 and eventos == 'altera':  # alterar status
        if listado == False:
            tp.msg = "Favor Lista e depois selecionar um Alunoa ser Alterado!"
            janela4 = tp.janela_popup_ok(tp.msg)
        else:
            bd.conection = bd.sqlite3.connect('bd.db')
            bd.c = bd.conection.cursor()
            ldd = valores['lido']
            dma = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            soma = sum(ldd)
            xd = dados_lidos
            cond = xd[soma][1]
            nv = valores['talterar']
            tu.nomec = xd[soma][2]
            tu.cpf = xd[soma][3]
            tu.sexo = xd[soma][4]
            tu.altura = xd[soma][5]
            tu.datan = xd[soma][6]
            tu.datem = xd[soma][1]  # t.datem      #xd[soma][1]#
            tu.peso = xd[soma][7]
            tu.status = tu.status
            dm = tc.datem
            n = tc.nomec
            cp = tc.cpf
            s = tc.sexo
            a = tc.altura
            d = tc.datan
            p = tc.peso
            st = tc.status
            tu.plano = bd.listaplano()
            tu.nomep = bd.listapersonal()
            # print(t.nomep)
            pl = tu.status
            ps = tu.nomep
            janela4 = tu.janela_cadastro_alt()
    if window == janela4 and eventos == 'alt_cad_aluno':
        bd.conection = bd.sqlite3.connect('bd.db')
        bd.c = bd.conection.cursor()
        dm = tu.datem
        n = tu.nomec
        cp = tu.cpf
        s = valores['sexo_alt']
        a = valores['altura_alt']
        d = valores['datan_alt']
        p = valores['peso_alt']
        st = valores['status_alt']
        pl = valores['plano_alt'][0]
        pers = valores['nomep'][0]
        # print(pers)
        ps = float(valores['peso_alt'].replace(',', '.'))
        al = float(valores['altura_alt'].replace(',', '.'))
        tt = ps / (al*al)
        im = valores['imc_alt'] = round(tt, 2)

        if valores['plano_alt'] == ".........." or valores['nomep'] == "..........":
            tp.msg = "Favor preencher todos os campos"
            janela5 = tp.janela_popup()

        else:
            tp.msg = "Tem Certeza?"
            janela5 = tp.janela_popup_upl(tp.msg)

    if window == janela5 and eventos == 'SIM.':
        bd.upl_novo(a, p, st, im, pl, pers, dm)
        bd.cadastrardados_h(n, cp, dma, s, a, d, p, im, st, pl, pers)
        window = janela3
        janela5.close()
        janela4.close()
        dados_lidos = bd.lista()
        window.find_element('lido').Update(dados_lidos)
        limpacampospersonal2()

    if window == janela5 and eventos == 'NÃO.':
        limpacampospersonal2()
        janela5.close()
        janela4.close()

    # pesquisa por nome aluno
    if window == janela3 and eventos == 'bt_pesquisa':
        pesquisa = valores['inp_pesquisa']
        pesquisa2 = "%"
        pesquisa3 = pesquisa2 + pesquisa + pesquisa2
        dados_lidos = bd.listacrit(pesquisa3)
        dados_lidos = bd.pesquisa(pesquisa3)
        if dados_lidos == []:
            tp.msg = "sem dados"
            janela4 = tp.janela_popup()
        else:
            window.find_element('lido').Update(dados_lidos)
            ldd = dados_lidos[0][1]
            cond = ldd
            nv = valores['talterar']
    if window == janela3 and eventos == 'bt_filtro':
        if valores['f_sexo'] == "TODOS":
            valores['f_sexo'] = "%"
            dados_lidos = bd.listacrit_filtros(
                valores['f_status'], valores['f_sexo'], valores['f_imcm'], valores['f_imc'], valores['b_plano'][0], valores['b_personal'][0])
            window.find_element('lido').Update(dados_lidos)

        if valores['f_status'] == "TODOS":
            valores['f_status'] = "%"
            dados_lidos = bd.listacrit_filtros(
                valores['f_status'], valores['f_sexo'], valores['f_imcm'], valores['f_imc'], valores['b_plano'][0], valores['b_personal'][0])
            window.find_element('lido').Update(dados_lidos)

        if valores['b_plano'] == "TODOS":
            valores['b_plano'] = "%"
            dados_lidos = bd.listacrit_filtros(
                valores['f_status'], valores['f_sexo'], valores['f_imcm'], valores['f_imc'], valores['b_plano'][0], valores['b_personal'][0])
            window.find_element('lido').Update(dados_lidos)

        if valores['b_personal'] == "TODOS":
            valores['b_personal'] = "%"
            dados_lidos = bd.listacrit_filtros(
                valores['f_status'], valores['f_sexo'], valores['f_imcm'], valores['f_imc'], valores['b_plano'][0], valores['b_personal'][0])
            window.find_element('lido').Update(dados_lidos)

            tm.reg = bd.listacrit_filtros_qtd(
                valores['f_status'], valores['f_sexo'], valores['f_imcm'], valores['f_imc'], valores['b_plano'][0], valores['b_personal'][0])
            msg = tm.reg[0][0]
            window.find_element('qdt_reg').Update(tm.reg[0][0])
        else:
            dados_lidos = bd.listacrit_filtros(
                valores['f_status'], valores['f_sexo'], valores['f_imcm'], valores['f_imc'], valores['b_plano'][0], valores['b_personal'][0])
            window.find_element('lido').Update(dados_lidos)

            tm.reg = bd.listacrit_filtros_qtd(
                valores['f_status'], valores['f_sexo'], valores['f_imcm'], valores['f_imc'], valores['b_plano'][0], valores['b_personal'][0])
            msg = tm.reg[0][0]
            window.find_element('qdt_reg').Update(tm.reg[0][0])

    # Chama atualizações planos
    if window == janela2 and eventos == 'Planos':
        janela3 = tu.ativosplanos()

        # LISTA TODOS planos
    if window == janela3 and eventos == 'listardadosplano':
        dados_lidosplano = bd.pesquisaplano()
        window.find_element('lidoplano').Update(dados_lidosplano)
        # print(dados_lidosplano)
        row_colors = ((0, 'white'))
        ev = eventos

        # LISTA PLANO ATIVOS
    if window == janela3 and eventos == 'ativosplano':
        critplano = "ATIVO"
        dados_lidosplano = bd.listacritplano(critplano)
        window.find_element('lidoplano').Update(dados_lidosplano)
        ev = eventos

        # Lista planos Inativos
    if window == janela3 and eventos == 'inativosplano':
        critplano = "INATIVO"
        dados_lidosplano = bd.listacritplano(critplano)
        window.find_element('lidoplano').Update(dados_lidosplano)
        ev = eventos

    # Delete plano
    if window == janela3 and eventos == 'deleteplano':  # deleta selecionado
        ld = valores['lidoplano']
        soma = sum(ld)
        x = dados_lidosplano
        y = x[soma][1]
        tu.a_peso = y
        tu.msg = "Confirmar a exclusão do Plano "+x[soma][2]
        janela4 = tu.janela_popup_delplano(tp.msg)
    if window == janela4 and eventos == 'simplano':
        bd.deleteselplano(y)
        window = janela3
        bd.pesquisaplano()
        dados_lidos = bd.pesquisaplano()
        janela4.close()
        window.find_element('lidoplano').Update(dados_lidosplano)
        window.find_element('lidoplano').Update(dados_lidosplano)
    if window == janela4 and eventos == 'naoplano':
        janela4.close()

     # Alterar cadastro de PLANOS
    if window == janela3 and eventos == 'alteraplano':  # alterar status
        bd.conection = bd.sqlite3.connect('bd.db')
        bd.c = bd.conection.cursor()
        ldd = valores['lidoplano']
        soma = sum(ldd)
        xd = dados_lidosplano
        tu.nomec = xd[soma][1]
        tu.user = xd[soma][2]
        tu.statusplano = xd[soma][3]
        janela4 = tu.janela_cad_plano_alt()
    if window == janela4 and eventos == 'alt_cad_plano':
        bd.conection = bd.sqlite3.connect('bd.db')
        bd.c = bd.conection.cursor()
        dm = tu.datem
        n = tu.nomec  # esse usar
        u = tu.user  # esse usar
        stp = valores['statusplano']
        tp.msg = "Tem Certeza?"
        janela5 = tp.janela_popup_uplplano(tp.msg)
    if window == janela5 and eventos == 'simaltplano':
        bd.upl_novoplano(stp, n)
        #print("n", n)
        #print("u", u)
        #print("stp", stp)
        window = janela3
        janela5.close()
        janela4.close()
        dados_lidos = bd.pesquisaplano()
        window.find_element('lidoplano').Update(dados_lidos)
    if window == janela5 and eventos == 'naoaltplano':
        janela5.close()
        janela4.close()

    # Atualizações personais
    if window == janela2 and eventos == 'Personais':
        janela3 = tu.ativospersonal()

    # LISTA TODOS PERSONAL
    if window == janela3 and eventos == 'listardadospersonal':
        dados_lidospersonal = bd.pesquisapersonal()
        window.find_element('lidopersonal').Update(dados_lidospersonal)
        # print(dados_lidospersonal)
        row_colors = ((0, 'white'))
        ev = eventos

    # LISTA PERSONAL ATIVOS
    if window == janela3 and eventos == 'ativospersonal':
        critpersonal = "ATIVO"
        dados_lidospersonal = bd.listacritpersonal(critpersonal)
        window.find_element('lidopersonal').Update(dados_lidospersonal)
        ev = eventos

    # LISTA PERSONAL INATIVOS
    if window == janela3 and eventos == 'inativospersonal':
        critpersonal = "INATIVO"
        dados_lidospersonal = bd.listacritpersonal(critpersonal)
        window.find_element('lidopersonal').Update(dados_lidospersonal)
        ev = eventos

    # Alterar cadastro de Personal
    if window == janela3 and eventos == 'alterapersonal':  # alterar status
        bd.conection = bd.sqlite3.connect('bd.db')
        bd.c = bd.conection.cursor()
        ldd = valores['lidopersonal']
        soma = sum(ldd)
        xd = dados_lidospersonal
        tu.nomec = xd[soma][1]
        tu.sexo = xd[soma][2]
        tu.altura = xd[soma][3]
        tu.datan = xd[soma][4]
        tu.peso = xd[soma][5]
        tu.statuspersonal = xd[soma][6]
        janela4 = tu.janela_cad_personal_alt()
    if window == janela4 and eventos == 'alt_cad_personal':
        bd.conection = bd.sqlite3.connect('bd.db')
        bd.c = bd.conection.cursor()
        n = tu.nomec
        at = valores['alturapersonal']
        ps = valores['pesopersonal']
        stp = valores['statuspersonal']
        tp.msg = "Tem Certeza?"
        janela5 = tp.janela_popup_uplpersonal(tp.msg)
    if window == janela5 and eventos == 'simaltpersonal':
        bd.upl_novopersonal(at, ps, stp, n)
        window = janela3
        janela5.close()
        janela4.close()
        dados_lidos = bd.pesquisapersonal()
        window.find_element('lidopersonal').Update(dados_lidos)
    if window == janela5 and eventos == 'naoaltpersonal':
        janela5.close()
        janela4.close()
