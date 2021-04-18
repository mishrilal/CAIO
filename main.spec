# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

added_files = [
         ( 'caio.db', '.' ),
         ( 'lockMain.py', '.' ),
         ( '/Users/mishrilal/Projects/CAIO/function/*.*', 'functions' ),
         ( 'qml/*.*', 'qml' ),
         ( 'qml/controls/*.*', 'qml/controls' ),
         ( 'qml/pages/*.*', 'qml/pages' ),
         ( '/mygame/sfx/*.mp3', 'sfx' )
         ]

a = Analysis(['main.py'],
             pathex=['/Users/mishrilal/Projects/CAIO'],
             binaries=[],
             datas=added_files,
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
          name='main',
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
               name='main')
app = BUNDLE(coll,
             name='CAIO.app',
             icon=images/svg_images/logo_icon.svg,
             bundle_identifier=com.mishrilal.caio)
