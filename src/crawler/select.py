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
        path = '../../res/dataset/other/bokeh_downloads/'
        path_clean = '../../res/dataset/y/bokeh_cleaned/'
        other_path_clean = '../../res/dataset/x/iphone_cleaned/'
    else:
        path = '../../res/dataset/other/iphone_downloads/'
        path_clean = '../../res/dataset/x/iphone_cleaned/'
        other_path_clean = '../../res/dataset/y/bokeh_cleaned/'

    if 'selecter' in kind:
        onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]

        onlyfiles.sort()
        keep = []
        change = []
        discard = []

        already_done = []

        with open('auto_'+task+'_discard.txt') as f:
            lines = [line.rstrip() for line in f]

            for line in lines:
                already_done.append(int(line))
        with open('auto_' + task + '_keep.txt') as f:
            lines = [line.rstrip() for line in f]

            for line in lines:
                already_done.append(int(line))
        with open('auto_' + task + '_change.txt') as f:
            lines = [line.rstrip() for line in f]

            for line in lines:
                already_done.append(int(line))

        count = 0
        for file in onlyfiles:
            number = ''.join(c for c in file if c.isdigit())

            if int(number) >= min_number and int(number) not in already_done:
                image = cv2.imread(path+file)
                print(path+file)
                cv2.imshow('image', image)
                key = cv2.waitKey(0)

                if key == ord('q'):
                    keep.append(number)
                elif key == ord('w'):
                    change.append(number)
                elif key == ord('e'):
                    discard.append(number)
                elif key == ord('l'):
                    break

                count += 1

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
        sub_path = 'bokeh_downloaded__' if 'bokeh' in task else 'iphone_downloaded__'

        with open('auto_'+task+'_keep.txt') as f:
            lines = [line.rstrip() for line in f]

            for line in lines:
                copyfile(path+sub_path+line+'.jpg', path_clean+str(line)+'.jpg')

        with open('auto_'+task+'_change.txt') as f:
            lines = [line.rstrip() for line in f]

            for line in lines:
                copyfile(path+sub_path+line+'.jpg', other_path_clean+str(line)+'_c.jpg')
