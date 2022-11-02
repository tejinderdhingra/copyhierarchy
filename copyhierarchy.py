"""
Utility to copy directory hirearchy
"""

import argparse
import shutil
import os

parser = argparse.ArgumentParser(prog = 'copyhierarchy', 
                                description = 'Duplicate a directory hierarchy')

parser.add_argument('-s', '--sourcedir',
                    dest ='srcdir',
                    type = str,
                    required = True,
                    metavar ='SRCDIR',
                    help = 'The root of a directory hierarchy to duplicate.')
parser.add_argument('-d', '--destdir',
                    dest ='destdir',
                    type = str,
                    required = True,
                    metavar ='DESTDIR',
                    help = 'The directory that will contain the duplicate.')

args = parser.parse_args()

def ignore_files(dir, files):
    """function to test if there are any files the directory"""
    return [f for f in files if os.path.isfile(os.path.join(dir, f))]

if not os.path.exists(args.srcdir):
    print(f'The source path "{args.srcdir}" does not exist.')
elif not os.path.isdir(args.srcdir):
    print(f'The source path "{args.srcdir}" is not a directory.')
elif not os.path.isdir(args.destdir):
    print(f'The destination path "{args.destdir}" is not a directory.')
elif os.path.exists(os.path.join(args.destdir, args.srcdir)):
    print(f'The destination path "{args.destdir}" already exists.')
else:
    shutil.copytree(args.srcdir, os.path.join(args.destdir, args.srcdir), ignore = ignore_files)
    print('Directory tree copied succesfully.')
