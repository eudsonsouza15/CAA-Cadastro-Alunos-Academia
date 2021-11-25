# @title Texto de título padrão { display-mode: "code" }

import getpass
from sys import maxsize
from tkinter.constants import CENTER
import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import ButtonMenu, Window, popup
import bd

from datetime import datetime
import calendar as cal
fnt = 'Arial 12'


status = ["ATIVO", "INATIVO"]
user = ""
ret_plano = []
ret_personal = []

#CONSULTA ALUNOS
def ativos_alunos_consulta():
    sg.theme(str(bd.tema)) 
    i = ""
    dados_lidos = [["", "", "", "", "", "", "", ""]]
    layout = [
        [sg.Table(
            key='lido',
            col_widths=[2, 13, 25, 8, 10, 6, 10, 5, 5, 8,12,25],
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
            "Delete", key="delete", expand_x=True,visible=False,border_width=3),
         sg.Combo(values=status, size=(10, 30), key='talterar', default_value="ATIVO",readonly=True), sg.Button(
            "Alterar", key='altera', expand_x=True,visible=False,border_width=3), sg.Input(key='inp_pesquisa'), sg.Button("Pesquisa", border_width=3,key='bt_pesquisa', expand_x=True),
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
    window = sg.Window('Menu Principal', layout=layout, finalize=True,
                       resizable=True, size=(0, 0), location=(-1, -1), modal=True)
    window.maximize()
    return window
    # return sg.Window('Atualizações dos alunos', layout=layout, finalize=True, size=(1100, 670), modal=True)
#CONULTA PLANOS


#CONSULTA PERSONAL

