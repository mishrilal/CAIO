import sys
from cx_Freeze import setup, Executable

files = ["functions/", "images/", "qml", "logo_icon.svg", "lockMain.py"]

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["os", "lockMain"], "excludes": ["tkinter", "PyQt5"], "include_files": files}

# GUI applications require a different base on Windows (the default is for
# a console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name="CAIO",
    version="0.1",
    description="Smart Lock",
    options={"build_exe": build_exe_options},
    executables=[Executable("main.py", base=base), Executable("lockMain.py", base=base)]
)
