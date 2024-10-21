#Joplin Export Script
# Kursadk

import subprocess
import shutil,os,glob
from pathlib import Path
import pathlib

PATH=Path(r"C:\CACHE\Joplin")
JOPLIN=Path("joplin")
CMD="export"
CMD_SYNC="sync"
LOG="--log-level"
LOGLEVEL="debug"
FORMAT="md_frontmatter"
NOTEBOOK="TUTORIAL"
NOTEBOOK=""
ARGS=["--format","--notebook"]

def remove_folder_contents(path):
    if os.path.exists(path):
        for root, dirs, files in os.walk(path):
            for file in files:
                os.remove(os.path.join(root, file))
            for dir in dirs:
                shutil.rmtree(os.path.join(root, dir))
        print(f"All contents of {path} removed successfully")
    else:
        print(f"{path} does not exist")

def rmContents(pth):
    path=pth.as_posix()
    print(path)
    files=pth.rglob("*")
    print(files)
    for f in files:
        if os.path.isfile(f):
            print(f)
            ff=pathlib.PureWindowsPath(f)
            f.unlink()
    remove_folder_contents(pth)

if PATH.exists():
    PATH.lstat()
    print("the path exists")
    rmContents(PATH)

else:
    PATH.mkdir()

PATH2=pathlib.PureWindowsPath(PATH).as_posix()
#JOPLIN SYNC
result=subprocess.run([JOPLIN,LOG,LOGLEVEL,CMD_SYNC], shell=True, capture_output=True, text=True)
print(result.stderr)
#JOPLIN EXPORT
result=subprocess.run([JOPLIN,CMD,PATH2,ARGS[0],FORMAT, ARGS[1],NOTEBOOK], shell=True, capture_output=True, text=True)
print(result.stdout)

