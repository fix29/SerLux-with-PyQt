# -*- mode: python -*-

block_cipher = None


a = Analysis(['SerLux.py'],
             pathex=['C:\\Users\\user\\Documents\\DX\\servo_ws\\tes-x\\siapkirim\\SerLux-with-PyQt'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='SerLux',
          debug=False,
          strip=False,
          upx=True,
          console=False , icon='C:\\Users\\user\\Documents\\DX\\servo_ws\\tes-x\\siapkirim\\SerLux-with-PyQt\\Images\\serlux.ico')
