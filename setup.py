
# setup.py
from cx_Freeze import setup, Executable
setup(
    name="Academia",
    options={"build_exe": {'packages': ["os","datetime","bd","PySimpleGUI","tkinter"],
    'include_files': ['Telas_Academia.py','bd.db','Principal.py','bd.py'],
    'include_msvcr': True}},
    executables=[Executable("Principal.py", base="Win32GUI")]
)


# executar   python setup.py bdist_msi

