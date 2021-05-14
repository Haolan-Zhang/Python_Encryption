import glob
import os
import shutil
import sys 
import py_compile
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('--dir', '-d', type=str, required=True, help='Please specify the project directory.')
parser.add_argument('--newDir', '-nd', type=str, default='', help='New project directory')
args = parser.parse_args()

path = repr(args.dir)[1:-1]
path2 = args.newDir 


def convert():
    # pys = []
    for root, dirs, files in os.walk(path2):
        for file in files:
            if file[-3:]==".py" :
                fullPath = os.path.join(root, file)
                # pys.append(fullPath)
                os.system(f"pyminifier -O --nonlatin -o {fullPath} {fullPath}")
                py_compile.compile(fullPath, cfile=fullPath.replace(".py", f".pyc"))
                os.remove(fullPath)
            
if path2 == '':
    path2 = f'{path}_new'

    if not os.path.exists(f'{path}_new'):
        shutil.copytree(path, f'{path}_new')
        convert()
    else:
        print('Please specify new file path!')
else:
    shutil.copytree(path, path2)
    convert()

print("请记下你python解释器的版本！此项目仅能用此版本python运行")
print(sys.version)