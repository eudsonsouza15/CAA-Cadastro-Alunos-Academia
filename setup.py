import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["os"], "includes": ["tkinter"]}

# GUI applications require a different base on Windows (the default is for
# a console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name="Academia",
    version="1.0",
    description="Cadastro de alunos",
    options={"build_exe": build_exe_options},
    executables=[Executable("main.py", base=base)]
)
# COMANDO PARA GERAR O EXECUTAVEL
#python .\setup.py build