# -*- mode: python ; coding: utf-8 -*-
import sys
import os
from kivy_deps import sdl2, glew
from kivymd import hooks_path as kivymd_hooks_path

block_cipher = None


a = Analysis(
    ['mdApp.py'],
    pathex=[],
    binaries=[],
    datas=[('mdAppComponents.kv', '.')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,Tree('D:\\Dir\\python\\Codemy\\KivyMD-Sandberg\\hotreload\\kivyTopBar\\'),
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
	*[Tree(p) for p in (sdl2.dep_bins + glew.dep_bins)],
    [],
    name='KivyMD',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
