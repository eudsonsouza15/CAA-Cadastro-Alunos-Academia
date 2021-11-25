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


# VARIAVES JANELAS
# janela1 = tc.janela_cadastro() #OK
# janela1 = tc.janela_cadastro_personal() # OK
# janela1 = tc.janela_cad_admin() #OK
# janela1 = tc.janela_cad_plano() #OK
# janela1 = tcs.ativos_alunos_consulta() #OK
# janela1 = tm.janela_login() #OK
# janela1 = tm.janelamenuadm() #OK
# janela1 = tm.janelamenuescrita() #OK
# janela1 = tm.janelamenueleitura() #OK
# janela1 = tu.janela_cad_personal_alt() #OK
# janela1 = tu.janela_cad_plano_alt() #OK
# janela1 = tu.janela_cadastro_alt() #OK
#janela1 = tu.ativos() #OK
#janela1 = tu.ativosplanos() #OK
janela1 = tu.ativospersonal() #OK


# Loop telas
while True:
    window, eventos, valores = sg.read_all_windows()
    if window == janela1 and eventos == sg.WIN_CLOSED:
        janela1.close()
