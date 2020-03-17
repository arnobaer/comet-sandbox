import os
import comet
from comet import utils

# Application name
name = 'comet-sandbox'

# Application organization
organization = 'HEPHY'

# Application version
version = comet.__version__

# Application package
module = 'app'

# Application datas
package_datas = []

# Application hidden imports
package_hiddenimports = []

# Windows version info template
version_info = """
VSVersionInfo(
    ffi=FixedFileInfo(
        filevers=({version[0]}, {version[1]}, {version[2]}, 0),
        prodvers=({version[0]}, {version[1]}, {version[2]}, 0),
        mask=0x3f,
        flags=0x0,
        OS=0x4,
        fileType=0x1,
        subtype=0x0,
        date=(0, 0)
    ),
    kids=[
        StringFileInfo(
            [
            StringTable(
                u'000004b0',
                [StringStruct(u'CompanyName', u'{organization}'),
                StringStruct(u'FileDescription', u'{name}'),
                StringStruct(u'FileVersion', u'{version[0]}.{version[1]}.{version[2]}.0'),
                StringStruct(u'InternalName', u'{name}'),
                StringStruct(u'LegalCopyright', u'GPLv3'),
                StringStruct(u'OriginalFilename', u'{name}.exe'),
                StringStruct(u'ProductName', u'{name}'),
                StringStruct(u'ProductVersion', u'{version[0]}.{version[1]}.{version[2]}.0'),
                ])
            ]),
        VarFileInfo([VarStruct(u'Translation', [0, 1200])])
    ]
)
"""

# Pyinstaller entry point template
entry_point = """
from {module} import main
import sys
if __name__ == '__main__':
    sys.exit(main())
"""

# Create pyinstaller entry point
with open('entry_point.pyw', 'w') as f:
    f.write(entry_point.format(
        module=module
    ))

# Create windows version info
with open('version_info.txt', 'w') as f:
    f.write(version_info.format(
        name=name,
        organization=organization,
        version=version.split('.'),
        license='GPLv3'
    ))

a = Analysis(['entry_point.pyw'],
    pathex=[
      os.getcwd()
    ],
    binaries=[],
    datas=[
        (utils.make_path('widgets', '*.ui'), os.path.join('comet', 'widgets')),
        (utils.make_path('assets', 'icons', '*.svg'), os.path.join('comet', 'assets', 'icons')),
        (utils.make_path('assets', 'icons', '*.ico'), os.path.join('comet', 'assets', 'icons')),
    ] + package_datas,
    hiddenimports=[
        'pyvisa-sim',
        'pyvisa-py',
        'PyQt5.sip',
    ] + package_hiddenimports,
    hookspath=[],
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=None,
    noarchive=False
)
pyz = PYZ(
    a.pure,
    a.zipped_data,
    cipher=None
)
exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name=name,
    version='version_info.txt',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=False,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    icon=utils.make_path('assets', 'icons', 'comet.ico'),
)
