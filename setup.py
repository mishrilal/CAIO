import sys
import numpy
import cv2
import PySide2
import sqlite3

from cx_Freeze import setup, Executable

includefiles = [('functions/', 'functions/'),
                ('images/', 'images/'),
                ('qml/', 'qml/'),
                ('logo_icon.svg','logo_icon.svg')
                ]

build_exe_options = {'packages': ['numpy'],
                     'excludes':['Tkinter'],
                     'include_files': includefiles
                     }
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(name = "CAIO",
      version = "0.0.65",
      description = "Lock App",
      options = {"build_exe": build_exe_options},
      executables = [Executable("main.py", base=base), Executable("lockMain.py", base=base)])