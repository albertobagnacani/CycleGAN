import os
from os.path import join
from pathlib import Path

from PIL import Image

if __name__ == "__main__":
    print('Making B&W')
    input_folder = '../../res/dataset/y/splitted/'
    output_folder = '../../res/dataset/x/splitted/'
    for name in ['train', 'test', 'val']:
        Path(join(output_folder, name, 'jpg')).mkdir(parents=True, exist_ok=True)

    root, dirs, files = next(os.walk(input_folder))
    for dir_ in dirs:
        root_n, dirs_n, files_n = next(os.walk(join(root, dir_, 'jpg')))

        for file in files_n:
            img = Image.open(join(root_n, file)).convert('L')
            img.save(join(output_folder, dir_, 'jpg', file))

    # TODO move train/val/test out of splitted, both in x and y
