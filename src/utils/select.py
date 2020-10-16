import os
from os import listdir
from os.path import isfile, join
from pathlib import Path
from shutil import copyfile

import cv2

if __name__ == '__main__':
    task = 'iphone'
    min_number = -1
    kind = 'merger'

    if 'bokeh' in task:
        path = 'bokeh_downloads/'
        path_clean = 'bokeh_cleaned/'
        other_path_clean = 'iphone_cleaned/'
    elif 'iphone' in task:
        path = 'iphone_downloads/'
        path_clean = 'iphone_cleaned/'
        other_path_clean = 'bokeh_cleaned/'
    else:
        path = 'helen/'
        path_clean = 'helen_cleaned/'
        other_path_clean = 'bokeh_cleaned/'

    if 'selecter' in kind:
        onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]

        onlyfiles.sort()
        keep = []
        change = []
        discard = []

        already_done = []

        if not os.path.exists('auto_'+task+'_discard.txt'):
            os.mknod('auto_'+task+'_discard.txt')
            os.mknod('auto_'+task+'_keep.txt')
            os.mknod('auto_'+task+'_change.txt')

        with open('auto_'+task+'_discard.txt') as f:
            lines = [line.rstrip() for line in f]

            for line in lines:
                already_done.append(line)
        with open('auto_' + task + '_keep.txt') as f:
            lines = [line.rstrip() for line in f]

            for line in lines:
                already_done.append(line)
        with open('auto_' + task + '_change.txt') as f:
            lines = [line.rstrip() for line in f]

            for line in lines:
                already_done.append(line)

        count = 0
        old_file = onlyfiles[0]
        last_click = 'q'
        for file in onlyfiles:
            # number = ''.join(c for c in file if c.isdigit())

            # if int(number) >= min_number and int(number) not in already_done:
            if file not in already_done:
                image = cv2.imread(path+file)
                print(path+file)
                cv2.namedWindow('image', cv2.WINDOW_NORMAL)
                cv2.imshow('image', image)
                key = cv2.waitKey(0)

                if key == ord('q'):
                    # keep.append(number)
                    keep.append(file)
                    last_click = 'q'
                elif key == ord('w'):
                    change.append(file)
                    last_click = 'w'
                elif key == ord('e'):
                    discard.append(file)
                    last_click = 'e'
                elif key == ord('r'):  # Undo
                    onlyfiles.insert(0, old_file)
                    onlyfiles.insert(1, file)

                    if last_click == 'q':
                        if len(keep) > 0:
                            del keep[-1]
                    elif last_click == 'w':
                        if len(change) > 0:
                            del change[-1]
                    elif last_click == 'e':
                        if len(discard) > 0:
                            del discard[-1]
                elif key == ord('l'):
                    break

                count += 1

                old_file = file

                # if count >= 5:
                #     break

        with open('auto_'+task+'_discard.txt', 'a') as f:
            for item in discard:
                f.write("%s\n" % item)
        with open('auto_'+task+'_keep.txt', 'a') as f:
            for item in keep:
                f.write("%s\n" % item)
        with open('auto_'+task+'_change.txt', 'a') as f:
            for item in change:
                f.write("%s\n" % item)
    else:
        Path(path_clean).mkdir(parents=True, exist_ok=True)
        Path(other_path_clean).mkdir(parents=True, exist_ok=True)
        sub_path = ''
        bis = ''
        ext = ''

        with open('auto_'+task+'_keep.txt') as f:
            lines = [line.rstrip() for line in f]

            for line in lines:
                copyfile(path+sub_path+line+ext, path_clean+bis+str(line)+ext)

        with open('auto_'+task+'_change.txt') as f:
            lines = [line.rstrip() for line in f]

            for line in lines:
                copyfile(path+sub_path+line+ext, other_path_clean+str(line[:-4] + '_c' + '.jpg')+ext)
