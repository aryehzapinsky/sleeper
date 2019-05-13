#!/usr/bin/env python3

import pathlib
import subprocess

p = pathlib.Path(".")
files_list = ([x for x in p.iterdir() if x.is_dir()])

for f in files_list:
    subprocess.run(['cd', '{}'.format(f)])

    current_parent = pathlib.Path(".")
    current_mp4 = current_parent.joinpath('{}.mp4'.format(f))

    if not current_mp4.exists():
        subprocess.run(['echo', '{}'.format(f)])
        subprocess.run(['concat_2'])

    subprocess.run(['cd', '..'])
