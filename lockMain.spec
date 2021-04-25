# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

includefiles = [('functions/lockFunctions.py', 'functions/lockFunctions.py')
                ]

a = Analysis(['lockMain.py'],
             pathex=['/Users/mishrilal/Projects/CAIO_MAIN'],
             binaries=[],
             datas=includefiles,
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='lockMain',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='lockMain')
app = BUNDLE(coll,
             name='lockMain.app',
             icon=None,
             bundle_identifier=None)
