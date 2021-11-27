from datetime import datetime
from datetime import date
import time
import bd
import PySimpleGUI as sg
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
    #=================================================================== 
    #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    #===================================================================
    # TELA LOGIN - ENTRAR
    if window == janela1 and eventos == 'Entrar':
        dadoslidos = bd.retlogin(valores['nome'])
        statement = f"SELECT user from admin WHERE user='{valores['nome']}' AND passs = '{valores['senha']}';"
        bd.c.execute(statement)
        if not bd.c.fetchone():
            ##print("Login failed")
            limpaadm()
            tp.msg = "Dados não conferem, favor tentar novamente"
            janela2 = tp.janela_popup()

        else:
            ##print("usurario", valores['nome'])
            ##print("dadoslidos", dadoslidos[0][0])
            bd.escolha = valores['escolha']
            print("tema é=====", valores['escolha'])
            print("escolha é ====", bd.escolha)
            print("bd tema é ===", bd.tema)
            if bd.escolha == "Claro":
                bd.tema = "SystemDefault1"
            if bd.escolha == "Escuro":
                bd.tema = "SandyBeach"
            if dadoslidos[0][0] == "Master":
                # #print("Welcome")
                janela1.close()
                janela2 = tm.janelamenuadm()

            if dadoslidos[0][0] == "Escrita":
                # #print("Welcome")
                janela1.close()
                janela2 = tm.janelamenuescrita()

            if dadoslidos[0][0] == "Leitura":
                # #print("Welcome")
                janela1.close()
                janela2 = tm.janelamenueleitura()
    #=================================================================== 
    #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    #===================================================================
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
                try:
                    p_peso_alt = float(valores['peso'].replace(',', '.'))
                    alt_alt = float(valores['altura'].replace(',', '.'))
                    peso_altura = p_peso_alt / (alt_alt*alt_alt)
                    valores['imc'] = round(peso_altura, 2)
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
                    #print("digite altura valida")
                    tp.msg = "Favor usar aplenas numeros para peso e alturapeso e altura validos"
                    janela4 = tp.janela_popup()
  

    if eventos == 'data':
        janela4 = sg.popup_get_date(start_year=1980, month_names=[
                                    "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Junho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"])
        if janela4:
            month, day, year = janela4
            window['datan'].update(f"{day:0>2d}/{month:0>2d}/{year}")
    #=================================================================== 
    #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    #===================================================================
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
    #=================================================================== 
    #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    #===================================================================
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
    #=================================================================== 
    #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    #===================================================================
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
    #=================================================================== 
    #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    #===================================================================
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
    #=================================================================== 
    #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    #===================================================================
    # CHAMA MENU CONSULTA alunos
    if window == janela2 and eventos == 'Consulta Alunos':
        tcs.plano = bd.listaplano()
        tcs.nomep = bd.listapersonal()
        tcs.plano.append("TODOS")
        tcs.nomep.append("TODOS")
        tcs.ret_plano = tcs.plano
        tcs.ret_personal = tcs.nomep
        janela3 = tcs.ativos_alunos_consulta()
        tm.i = 0
    #=================================================================== 
    #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    #===================================================================    
        # LISTA TODOS ALUNOS
    if window == janela3 and eventos == 'listardados':
        listado = True
        # #print(listado)
        dados_lidos = bd.lista()
        window.find_element('lido').Update(dados_lidos)
        row_colors = ((0, 'white'))
    #=================================================================== 
    #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    #===================================================================
        # LISTA ALUNOS ATIVOS
    if window == janela3 and eventos == 'ativos':
        listado = True
        criterio = "ATIVO"
        dados_lidos = bd.listacrit(criterio)
        window.find_element('lido').Update(dados_lidos)
    #=================================================================== 
    #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    #===================================================================
        # LISTA ALUNOS INATIVOS
    if window == janela3 and eventos == 'inativos':  # lista alunos inativos
        listado = True
        criterio = "INATIVO"
        dados_lidos = bd.listacrit(criterio)
        window.find_element('lido').Update(dados_lidos)
    #=================================================================== 
    #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    #===================================================================
    # DELETA DADOS alunos
    if window == janela3 and eventos == 'delete':  # deleta selecionado

        if listado == False:
            tp.msg = "Favor Lista e depois selecionar um Alunoa ser deletado!"
            janela4 = tp.janela_popup_ok(tp.msg)
            ##print("ao fechar",listado)
        else:
            vl_lido = valores['lido']
            soma = sum(vl_lido)
            x_d_lido = dados_lidos
            #print("dadoslidos>>>>>>>>>>>>>>>>>>>>>>>>>",dados_lidos)
            if x_d_lido != []:
                y_d_lido = x_d_lido[soma][1]
                #print("y_d_lido>>>>>>>>>>>>>>>>>>>>>>>>>",y_d_lido)
                tu.a_peso = y_d_lido
                tp.msg = "Confirmar alt_alterar exclusão do aluno " + \
                x_d_lido[soma][2]
                janela4 = tp.janela_popup_del(tp.msg)
            else:
                tp.msg = "Favor Lista e depois selecionar um Alunoa ser deletado!"
                janela4 = tp.janela_popup_ok(tp.msg)    

    if window == janela4 and eventos == 'SIM':
        bd.deletesel(y_d_lido)
        window = janela3
        bd.lista()
        dados_lidos = bd.lista()
        window.find_element('lido').Update(dados_lidos)
        janela4.close()
        window.find_element('lido').Update(dados_lidos)
    if window == janela4 and eventos == 'NÃO':
        janela4.close()
    #=================================================================== 
    #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    #===================================================================
    # Alterar cadastro de alunos
    if window == janela3 and eventos == 'altera':  # alterar status
        if listado == False:
            tp.msg = "Favor Lista e depois selecionar um Alunoa ser Alterado!"
            janela4 = tp.janela_popup_ok(tp.msg)
        else:
            bd.conection = bd.sqlite3.connect('bd.db')
            bd.c = bd.conection.cursor()
            ld_lido = valores['lido']
            d_mov = datetime.now().strftime("%data_n_alt/%m/%Y %H:%M:%S")
            soma = sum(ld_lido)
            x_d_lido = dados_lidos
            cond = x_d_lido[soma][1]
            nv_val_alterar = valores['talterar']
            tu.nomec = x_d_lido[soma][2]
            tu.cpf = x_d_lido[soma][3]
            tu.sexo = x_d_lido[soma][4]
            tu.altura = x_d_lido[soma][5]
            tu.datan = x_d_lido[soma][6]
            tu.datem = x_d_lido[soma][1]  # t.datem      #x_d_lido[soma][1]#
            tu.peso = x_d_lido[soma][7]
            tu.status = tu.status
            d_mov = tc.datem
            nome_c = tc.nomec
            c_p_f = tc.cpf
            s_sexo = tc.sexo
            alt_alterar = tc.altura
            data_n_alt = tc.datan
            peso_alterado = tc.peso
            stat_alterado = tc.status
            tu.plano = bd.listaplano()
            tu.nomep = bd.listapersonal()
            # #print(t.nomep)
            p_plano_alt = tu.status
            p_peso_alt = tu.nomep
            list1 = list(p_peso_alt)
            # print(list1)

            janela4 = tu.janela_cadastro_alt()
    if window == janela4 and eventos == 'alt_cad_aluno':
        bd.conection = bd.sqlite3.connect('bd.db')
        bd.c = bd.conection.cursor()
        d_mov = tu.datem
        nome_c = tu.nomec
        c_p_f = tu.cpf
        s_sexo = valores['sexo_alt']
        alt_alterar = valores['altura_alt']
        data_n_alt = valores['datan_alt']
        peso_alterado = valores['peso_alt']
        stat_alterado = valores['status_alt']
        p_plano_alt = valores['plano_alt'][0]
        pers_alterado = valores['nomep'][0]

        p_peso_alt = float(valores['peso_alt'].replace(',', '.'))
        alt_alt = float(valores['altura_alt'].replace(',', '.'))
        peso_altura = p_peso_alt / (alt_alt*alt_alt)
        imc_atual = valores['imc_alt'] = round(peso_altura, 2)

        if valores['plano_alt'] == ".........." or valores['nomep'] == "..........":
            tp.msg = "Favor preencher todos os campos"
            janela5 = tp.janela_popup()

        else:
            tp.msg = "Tem Certeza?"
            janela5 = tp.janela_popup_upl(tp.msg)

    if window == janela5 and eventos == 'SIM.':
        bd.upl_novo(alt_alterar, peso_alterado, stat_alterado,
                    imc_atual, p_plano_alt, pers_alterado, d_mov)
        bd.cadastrardados_h(nome_c, c_p_f, d_mov, s_sexo, alt_alterar, data_n_alt,
                            peso_alterado, imc_atual, stat_alterado, p_plano_alt, pers_alterado)
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
    #=================================================================== 
    #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    #===================================================================
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
            ld_lido = dados_lidos[0][1]
            cond = ld_lido
            nv_val_alterar = valores['talterar']
    #=================================================================== 
    #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    #===================================================================
    # Filtos alunos      

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
    #=================================================================== 
    #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    #===================================================================
    # Chama atualizações planos
    if window == janela2 and eventos == 'Planos':
        janela3 = tu.ativosplanos()
    #=================================================================== 
    #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    #===================================================================
        # LISTA TODOS planos
    if window == janela3 and eventos == 'listardadosplano':

        dados_lidosplano = bd.pesquisaplano()
        window.find_element('lidoplano').Update(dados_lidosplano)
        row_colors = ((0, 'white'))
    #=================================================================== 
    #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    #===================================================================
        # LISTA PLANO ATIVOS
    if window == janela3 and eventos == 'ativosplano':
        critplano = "ATIVO"
        dados_lidosplano = bd.listacritplano(critplano)
        window.find_element('lidoplano').Update(dados_lidosplano)
    #=================================================================== 
    #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    #===================================================================
        # Lista planos Inativos
    if window == janela3 and eventos == 'inativosplano':
        critplano = "INATIVO"
        dados_lidosplano = bd.listacritplano(critplano)
        window.find_element('lidoplano').Update(dados_lidosplano)
    #=================================================================== 
    #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    #===================================================================
    # Delete plano
    if window == janela3 and eventos == 'deleteplano':  # deleta selecionado
        vl_lido = valores['lidoplano']
        soma = sum(vl_lido)
        x_d_lido = dados_lidosplano
        y_d_lido = x_d_lido[soma][1]
        tu.a_peso = y_d_lido
        tp.msg = "Confirmar alt_alterar exclusão do Plano "+x_d_lido[soma][2]
        janela4 = tp.janela_popup_delplano(tp.msg)
    if window == janela4 and eventos == 'simplano':
        bd.deleteselplano(y_d_lido)
        window = janela3
        bd.pesquisaplano()
        dados_lidosplano = bd.pesquisaplano()
        window.find_element('lidoplano').Update(dados_lidosplano)
        janela4.close()

    if window == janela4 and eventos == 'naoplano':
        janela4.close()
    #=================================================================== 
    #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    #===================================================================
     # Alterar cadastro de PLANOS
    if window == janela3 and eventos == 'alteraplano':  # alterar status
        bd.conection = bd.sqlite3.connect('bd.db')
        bd.c = bd.conection.cursor()
        ld_lido = valores['lidoplano']
        soma = sum(ld_lido)
        x_d_lido = dados_lidosplano
        tu.nomec = x_d_lido[soma][1]
        tu.user = x_d_lido[soma][2]
        tu.statusplano = x_d_lido[soma][3]
        janela4 = tu.janela_cad_plano_alt()
    if window == janela4 and eventos == 'alt_cad_plano':
        bd.conection = bd.sqlite3.connect('bd.db')
        bd.c = bd.conection.cursor()
        d_mov = tu.datem
        nome_c = tu.nomec  # esse usar
        u_user = tu.user  # esse usar
        stp = valores['statusplano']
        tp.msg = "Tem Certeza?"
        janela5 = tp.janela_popup_uplplano(tp.msg)
    if window == janela5 and eventos == 'simaltplano':
        bd.upl_novoplano(stp, nome_c)
        ##print("nome_c", nome_c)
        ##print("u_user", u_user)
        ##print("stp", stp)
        window = janela3
        janela5.close()
        janela4.close()
        dados_lidos = bd.pesquisaplano()
        window.find_element('lidoplano').Update(dados_lidos)
    if window == janela5 and eventos == 'naoaltplano':
        janela5.close()
        janela4.close()

    #=================================================================== 
    #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    #===================================================================
        # pesquisa por nome plano
    if window == janela3 and eventos == 'bt_pesquisaplano':
        pesquisaPlano = valores['inp_pesquisaplano']
        pesquisa2 = "%"
        pesquisa_plano = pesquisa2 + pesquisaPlano + pesquisa2
        dados_lidos_pes_plano = bd.listacrit(pesquisa_plano)
        dados_lidos_pes_plano = bd.pesquisa_plano(pesquisa_plano)
        if dados_lidos_pes_plano == []:
            tp.msg = "sem dados"
            janela4 = tp.janela_popup()
        else:
            window.find_element('lidoplano').Update(dados_lidos_pes_plano)
            ld_lidoplano = dados_lidos_pes_plano[0][1]
            cond = ld_lidoplano
            nv_val_alterarplano = valores['talterarplano']
    #=================================================================== 
    #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    #=================================================================== 
    # Atualizações personais
    if window == janela2 and eventos == 'Personais':
        janela3 = tu.ativospersonal()
    #=================================================================== 
    #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    #=================================================================== 
        # Consula personais
    if window == janela2 and eventos == 'Consulta Personais':
        janela3 = tcs.consulta_personal()

    #=================================================================== 
    #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    #===================================================================
    # LISTA TODOS PERSONAL
    if window == janela3 and eventos == 'listardadospersonal':
        dados_lidospersonal = bd.pesquisapersonal()
        window.find_element('lidopersonal').Update(dados_lidospersonal)
        # print(dados_lidospersonal)
        row_colors = ((0, 'white'))
    #=================================================================== 
    #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    #=================================================================== 
    # LISTA PERSONAL ATIVOS
    if window == janela3 and eventos == 'ativospersonal':
        critpersonal = "ATIVO"
        dados_lidospersonal = bd.listacritpersonal(critpersonal)
        window.find_element('lidopersonal').Update(dados_lidospersonal)
    #=================================================================== 
    #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    #===================================================================
    # LISTA PERSONAL INATIVOS
    if window == janela3 and eventos == 'inativospersonal':
        critpersonal = "INATIVO"
        dados_lidospersonal = bd.listacritpersonal(critpersonal)
        window.find_element('lidopersonal').Update(dados_lidospersonal)
    #=================================================================== 
    #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    #===================================================================
    # Alterar cadastro de Personal
    if window == janela3 and eventos == 'alterapersonal':  # alterar status
        bd.conection = bd.sqlite3.connect('bd.db')
        bd.c = bd.conection.cursor()
        ld_lido = valores['lidopersonal']
        soma = sum(ld_lido)
        x_d_lido = dados_lidospersonal
        tu.nomec = x_d_lido[soma][1]
        tu.sexo = x_d_lido[soma][2]
        tu.altura = x_d_lido[soma][3]
        tu.datan = x_d_lido[soma][4]
        tu.peso = x_d_lido[soma][5]
        tu.statuspersonal = x_d_lido[soma][6]
        janela4 = tu.janela_cad_personal_alt()
    if window == janela4 and eventos == 'alt_cad_personal':
        bd.conection = bd.sqlite3.connect('bd.db')
        bd.c = bd.conection.cursor()
        nome_c = tu.nomec
        at = valores['alturapersonal']
        p_peso_alt = valores['pesopersonal']
        stp = valores['statuspersonal']
        tp.msg = "Tem Certeza?"
        janela5 = tp.janela_popup_uplpersonal(tp.msg)
    if window == janela5 and eventos == 'simaltpersonal':
        bd.upl_novopersonal(at, p_peso_alt, stp, nome_c)
        window = janela3
        janela5.close()
        janela4.close()
        dados_lidos = bd.pesquisapersonal()
        window.find_element('lidopersonal').Update(dados_lidos)
    if window == janela5 and eventos == 'naoaltpersonal':
        janela5.close()
        janela4.close()
    #=================================================================== 
    #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    #===================================================================
        # Delete personal
    if window == janela3 and eventos == 'deletepersona':  # deleta personal
        ldpersonal = valores['lidopersonal']
        soma = sum(ldpersonal)
        x_d_lido = dados_lidospersonal
        y_d_lido = x_d_lido[soma][1]

        #print("x_d_lido", x_d_lido)
        #print("y_d_lido", y_d_lido)

        tp.msg = "Confirmar alt_alterar exclusão do Personal: "+y_d_lido
        janela4 = tp.janela_popup_delpersonal(tp.msg)
    if window == janela4 and eventos == 'simpersonal':
        bd.deleteselpersonal(y_d_lido)
        window = janela3
        bd.pesquisapersonal()
        dados_lidospersonal = bd.pesquisapersonal()
        window.find_element('lidopersonal').Update(dados_lidospersonal)
        janela4.close()

    if window == janela4 and eventos == 'naopersonal':
        janela4.close()
        dados_lidospersonal = bd.pesquisapersonal()
        # window.find_element('lidopersonal').Update(dados_lidospersonal)
        # print(dados_lidospersonal)
        row_colors = ((0, 'white'))
    #=================================================================== 
    #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
      
