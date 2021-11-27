# @title Texto de título padrão { display-mode: "code" }


from tkinter.constants import CENTER
import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import ButtonMenu, Window, popup
import bd

from datetime import datetime
import calendar as cal
fnt = 'Arial 12'



nomec = ""
nomep = ""
cpf =""
altura = ""
peso = ""
datan = ""
sexo = ["MASCULINO", "FEMENINO"]
status = ["ATIVO", "INATIVO"]
imc = ""
user = ""
datem = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
plano = []
ret_plano = []
ret_personal = []




#Alterar Cadastro personal
def janela_cad_personal_alt():
    sg.theme(str(bd.tema)) 
    cadastros = [
        [sg.Text("Nome completo"), sg.Input(
            nomec, key='nomeppersonal', expand_x=True, disabled=True)],
        [sg.Text("Sexo"), sg.Input(sexo, size=(20, 30), key='sexopersonal', disabled=True),
            sg.Text("Data Mov."), sg.Input(datem, key='datempersonal', disabled=True, size=(20, 30), expand_x=True)],
        [sg.Text("Altura"), sg.Input(altura, key='alturapersonal', size=(8, 30)), sg.Text("Data nascimento"),
            sg.Input(datan, key='datanpersonal', size=(10, 30), disabled=True), sg.Button("Data Nascimento", key='datapersonal', expand_x=True, disabled=True,border_width=3)],
        [sg.Text("Peso"), sg.Input(peso, key='pesopersonal', size=(8, 30)),
            sg.Input(imc, key='imcpersonal', disabled=True, size=(8, 30),
                     visible=False), sg.Text("              Statuspersonal"),
            sg.Combo(values=status, key='statuspersonal', size=(20, 30), expand_x=True, default_value="ATIVO",readonly=True)],


        [sg.Button('Alterar', key='alt_cad_personal',border_width=3), sg.Button('  Sair  ',border_width=3)]
    ]
    return sg.Window('Tela Alterar Cadastro de Personal', layout=cadastros, finalize=True, modal=True,keep_on_top=True)

# Alterar cadastro de planos
def janela_cad_plano_alt():
    sg.theme(str(bd.tema)) 
    cad_plano = [
        [sg.Text("Nome plano"), sg.Input(
            nomec, key='nomeplano', disabled=True,expand_x=True)],
        [sg.Text("Codigo Plano"), sg.Input(
            user, key='codplano', disabled=True)],
        [sg.Text("Status plano"), sg.Combo(status, key='statusplano',readonly=True,size=(15,10))],
        [sg.Button('Alterar', key='alt_cad_plano',border_width=3), sg.Button('  Sair  ',border_width=3)]
    ]
    return sg.Window('Alteração Cadastro de plano', layout=cad_plano, finalize=True, modal=True,keep_on_top=True)


# Tela Altera cadastro aluno


def janela_cadastro_alt():
    sg.theme(str(bd.tema)) 
    cadastros = [
        [sg.Text("Nome completo"), sg.Input(
            nomec, key='nomec_alt', size=(45,10),disabled=True,expand_x=True)],
        [sg.Text("CPF"), sg.Input(cpf, key='cpf_alt', size=(20, 30),expand_x=False,disabled=True), sg.Text("Data Mov."), sg.Input(datem, key='datem_alt', disabled=True, size=(20, 30),expand_x=True)],    
        [sg.Text("Sexo"), sg.Input(sexo, disabled=True, size=(20, 30), key='sexo_alt'),
            sg.Text("Data nascimento"), sg.Input(datan, key='datan_alt', size=(15, 30), disabled=True,expand_x=True)],
        [sg.Text("Altura"), sg.Input(altura, key='altura_alt', size=(8, 30)), sg.Text("Peso"), sg.Input(peso, key='peso_alt', size=(8, 30)), sg.Input(imc, key='imc_alt', disabled=True, size=(8, 30), visible=False), sg.Text("Status"),
            sg.Combo(values=status, key='status_alt', size=(
                20, 30), expand_x=True, default_value="ATIVO",readonly=True)
            ],
            [sg.Text("Plano "),sg.Combo(values=plano, key='plano_alt',
                     size=(20, 30), expand_x=False,default_value="..........",readonly=True),
            sg.Text("Personal "),sg.Combo(values=nomep, key='nomep', size=(20, 30), expand_x=True,default_value="..........",readonly=True)],

        [sg.Button('Aterar', key='alt_cad_aluno',border_width=3), sg.Button('  Sair  ',border_width=3)]
    ]
    return sg.Window('Alteração de Cadastro de Aluno', layout=cadastros, finalize=True, modal=True, keep_on_top=True)



def ativos():
    sg.theme(str(bd.tema)) 
    i = ""
    dados_lidos = [["", "", "", "", "", "", "", ""]]
    layout = [
        [sg.Table(
            key='lido',
            col_widths=[2, 13, 25, 10, 10, 6, 10, 5, 5, 8,12,23],
            values=dados_lidos,
            headings=["ID", "Data Mov.", "Nome","CPF", "Sexo", "Altura",
                      "Dt Nascimento", "Peso", "IMC", "Status", "Plano", "Personl"],
            # row_colors=[(i,cor)],
            row_colors=[(i, 'red', 'green')],  # for i in range(0,  19)],
            justification='left',
            max_col_width=20,
            auto_size_columns=False,
            #background_color='#aaaaaa',
            header_background_color='#aaaaaa',
            alternating_row_color='#E0F2F7',
            expand_x=True,
            expand_y=True,
            # def_col_width=15,
            text_color='black',

        )],
        [sg.Text('')],
        [sg.Button("Listar Todos", key="listardados", expand_x=True,border_width=3), sg.Button("Ativos", key="ativos", expand_x=True,border_width=3),
         sg.Button("Inativos", key="inativos", expand_x=True,border_width=3), sg.Button(
            "Delete", key="delete", expand_x=True,border_width=3),
         sg.Combo(values=status, size=(10, 30), key='talterar', default_value="ATIVO",readonly=True), sg.Button(
            "Alterar", key='altera', expand_x=True,border_width=3), sg.Input(key='inp_pesquisa'), sg.Button("Pesquisa", key='bt_pesquisa', expand_x=True,border_width=3),
         ],
        [sg.Text('F i l t r a r  D a d o s======================================================================================================================')],
        [sg.Text('Status'), sg.Combo(("ATIVO", "INATIVO", "TODOS"), default_value="TODOS", size=(8, 30), key='f_status',readonly=True),
         sg.Text('  Sexo'),
         sg.Combo(values=("MASCULINO", "FEMENINO", "TODOS"), default_value="TODOS", size=(
             15, 30), key='f_sexo', change_submits=True,readonly=True),
         sg.Text("  Imc >="), sg.Input(key='f_imcm', size=(
             5, 30), default_text=1), sg.Text("  Imc <="),
         sg.Input(key='f_imc', size=(5, 30),
                  default_text=100), sg.Text("  Plano"),
         sg.Combo(values=ret_plano, key='b_plano', size=(15, 30),
                  default_value="TODOS",readonly=True), sg.Text("  Personal"),
         sg.Combo(values=ret_personal, key='b_personal',
                  size=(15, 30), default_value="TODOS",readonly=True),
         sg.Button(" Filtrar dados", key='bt_filtro',border_width=3)],
        [sg.Text("Total de Registos da consuta", font=30), sg.Input(
            key='qdt_reg', size=(5, 30), disabled=True, justification='center', font=30)],

        [sg.Text('=====================================================================================================================================')]
    ]
    window = sg.Window('Atualizações Alunos', layout=layout, finalize=True,
                       resizable=True, size=(0, 0), location=(-1, -1), modal=True)
    window.maximize()
    return window
    # return sg.Window('Atualizações dos alunos', layout=layout, finalize=True, size=(1100, 670), modal=True)


# Tela Atualizações Planos
def ativosplanos():
    sg.theme(str(bd.tema)) 
    i = ""
    dados_lidosplano = [["", "", "", "", "", "", "", ""]]
    layout = [
        [sg.Table(
            key='lidoplano',
            col_widths=[10, 10],
            values=dados_lidosplano,
            headings=["ID", "Nome Plano", "Cod. Plano", "Status Plano"],
            # row_colors=[(i,cor)],
            row_colors=[(i, 'red', 'green')],  # for i in range(0,  19)],
            justification='left',
            max_col_width=20,
            auto_size_columns=False,
            # background_color='#aaaaaa',
            header_background_color='#aaaaaa',
            alternating_row_color='#E0F2F7',
            expand_x=True,
            expand_y=True,
            # def_col_width=15,
            text_color='black',

        )],
        [sg.Text('')],
        [sg.Button("Listar Todos", key="listardadosplano", expand_x=True,border_width=3), sg.Button("Ativos", key="ativosplano", expand_x=True, disabled=False,border_width=3),
         sg.Button("Inativos", key="inativosplano", expand_x=True, disabled=False,border_width=3), sg.Button(
            "Delete", key="deleteplano", expand_x=True,border_width=3),
         sg.Combo(values=status, size=(10, 30), key='talterarplano', default_value="ATIVO",readonly=True), sg.Button(
            "Alterar", key='alteraplano', expand_x=True), sg.Input(user, key='inp_pesquisaplano'), sg.Button("Pesquisa", key='bt_pesquisaplano', expand_x=True,border_width=3),
         ]]
    window = sg.Window('Atualização de planos', layout=layout, finalize=True,
                       resizable=True, size=(0, 0), location=(-1, -1), modal=True)
    window.maximize()
    return window
    #return sg.Window('Atualização planos', layout=layout, finalize=True, size=(1100, 550), modal=True)

# Atualizações Personais


def ativospersonal():
    sg.theme(str(bd.tema)) 
    i = ""
    dados_lidospersonal = [["", "", "", "", "", "", "", ""]]
    layout = [
        [sg.Table(
            key='lidopersonal',
            col_widths=[10, 10, 10, 10, 10, 10, 10],
            values=dados_lidospersonal,
            headings=["ID", "Nome Personal", "Sexo", "Altura",
                      "Data de nascimento", "Peso", "Status"],
            # row_colors=[(i,cor)],
            row_colors=[(i, 'red', 'green')],  # for i in range(0,  19)],
            justification='left',
            max_col_width=20,
            auto_size_columns=False,
            # background_color='#aaaaaa',
            header_background_color='#aaaaaa',
            alternating_row_color='#E0F2F7',
            expand_x=True,
            expand_y=True,
            # def_col_width=15,
            text_color='black',

        )],
        [sg.Text('')],
        [sg.Button("Listar Todos", key="listardadospersonal", expand_x=True,border_width=3), sg.Button("Ativos", key="ativospersonal", expand_x=True, disabled=False,border_width=3),
         sg.Button("Inativos", key="inativospersonal", expand_x=True, disabled=False,border_width=3), sg.Button(
            "Delete", key="deletepersona", expand_x=True, disabled=False,border_width=3),
         sg.Combo(values=status, size=(10, 30), key='talterarpersonal', default_value="ATIVO", disabled=False,readonly=True), sg.Button(
            "Alterar", key='alterapersonal', expand_x=False,border_width=3), sg.Input(user, key='inp_pesquisapersonal', disabled=False), sg.Button("Pesquisa", key='bt_pesquisapersonal', expand_x=True, disabled=False,border_width=3),
         ]]
    window = sg.Window('Atualização de personal', layout=layout, finalize=True,
                       resizable=True, size=(0, 0), location=(-1, -1), modal=True)
    window.maximize()
    return window
    #return sg.Window('Atualização personal', layout=layout, finalize=True, size=(1100, 550), modal=True)