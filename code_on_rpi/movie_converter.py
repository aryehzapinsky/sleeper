#!/usr/bin/env python3

# Run on raspberry pi

import pathlib
import subprocess
import os

dirpath = os.getcwd()
p = pathlib.Path(dirpath)
files_list = ([str(x) for x in p.iterdir() if x.is_dir()])

for f in files_list:
    current_path = p.joinpath(f)
    os.chdir(str(current_path))
    file_name = current_path.stem
    current_mp4 = current_path.joinpath('{}.mp4'.format(file_name))
    #subprocess.run(['cd', '{}'.format(f)], shell=True)

    if not current_mp4.exists():
        #subprocess.run(['echo', '{}'.format(f)], shell=True)
        print(current_mp4)
        subprocess.run(['/media/pi/Snorlax/code/concatenate_videos_2.sh'], shell=True)

    os.chdir(dirpath)
    #subprocess.run(['cd', '..'], shell=True)
