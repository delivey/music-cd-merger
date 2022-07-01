import os
from pathlib import Path


def merge_cds(folder, replace_n, pad):
    p = Path(folder)
    cds = [str(f) for f in p.iterdir() if f.is_dir()]

    file_index = 0
    for cd in cds:
        files = os.listdir(cd)
        for file in files:
            file_index += 1
            new_filename = str(file_index).zfill(pad) + file[replace_n:]
            os.rename(f'{cd}/{file}', f'{folder}/{new_filename}')
        os.rmdir(cd)