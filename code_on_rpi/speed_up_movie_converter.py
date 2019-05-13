#!/usr/bin/env python3

# Run on Mac from videos folder

import pathlib
import subprocess
import os

dirpath = os.getcwd()
p = pathlib.Path(dirpath)
files_list = ([str(x) for x in p.iterdir() if x.is_dir()])

par_path = os.pardir

for f in files_list:
    current_path = p.joinpath(f)
    # os.chdir(str(current_path))
    file_name = current_path.stem
    current_mp4 = current_path.joinpath('{}.mp4'.format(file_name))
    sped_up_file_name = os.path.abspath(os.path.join(par_path,
                "sped_up_videos/{}_120x_60fps.mp4".format(current_mp4.stem)))
    sped_up_file_path = pathlib.Path(sped_up_file_name)

    if current_mp4.exists() and not sped_up_file_path.exists():
        #subprocess.run(['echo', '{}'.format(f)], shell=True)
        print(current_mp4)
        command = "ffmpeg -i {previous} -r 60 -filter:v \"setpts=0.0083*PTS\" {sped_up} -an".format(previous=current_mp4, sped_up=sped_up_file_name)
        subprocess.run([command], shell=True)

    os.chdir(dirpath)
