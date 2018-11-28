import os
from shutil import copyfile

BASEDIR = os.path.dirname(os.path.abspath(__file__))
FILES = ['gtkssw.py', 'stopwatch.png']

def main():
    home_folder = os.getenv('HOME')
    app_folder = os.path.join(home_folder, '.Stopwatch')
    if not os.path.exists(app_folder):
        os.makedirs(app_folder)
    for f in FILES:
        copyfile(os.path.join(BASEDIR, f), os.path.join(app_folder, f))
    desktop = '''[Desktop Entry]
Version=1.0
Name=Stopwatch
Exec=python3 {fp}/gtkssw.py
Icon={fp}/stopwatch.png
Path={fp}/
Terminal=false
Type=Application
Categories=Utility;Application;
'''.format(fp=app_folder)
    with open(os.path.join(home_folder, '.local', 'share', 'applications', 'Stopwatch.desktop'), 'w') as f:
        f.write(desktop)


if __name__ == '__main__':
    main()
