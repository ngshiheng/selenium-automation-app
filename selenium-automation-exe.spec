# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['main.py'],
             pathex=['C:\\Users\\ngshi\\Documents\\Personal\\selenium-automation-app'],
             binaries=[('driver\\chromedriver.exe', 'driver\\')],
             datas=[('example.json', '.'), ('example.ini', '.')],
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
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='selenium-automation-exe',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True , icon='favicon.ico')

import shutil
shutil.copyfile('example.ini', '{0}/example.ini'.format(DISTPATH))
shutil.copyfile('example.json', '{0}/example.json'.format(DISTPATH))