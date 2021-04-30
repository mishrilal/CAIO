import sys
from cx_Freeze import setup, Executable

files = ["functions/", "images/", "qml", "logo_icon.svg", "lockMain.py", "lockMain.ico", "logo_icon.ico"]

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["os", "lockMain"], "excludes": ["tkinter", "PyQt5"], "include_files": files}

# GUI applications require a different base on Windows (the default is for
# a console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

target = [Executable(
    script="CAIO.py",
    base=base,
    icon="logo_icon.ico"
),
    Executable(
        script="CAIO Lock.py",
        base=base,
        icon="lockMain.ico"
    )
]

setup(
    name="CAIO",
    version="0.1.45",
    description="Smart Lock",
    options={"build_exe": build_exe_options},
    executables=target
)
