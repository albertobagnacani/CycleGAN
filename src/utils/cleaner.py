import os
from multiprocessing.pool import Pool

from PIL import Image


def is_grayscale(fn):
    img = Image.open(fn).convert('RGB')

    w, h = img.size
    for i in range(w):
        for j in range(h):
            r, g, b = img.getpixel((i, j))
            if r != g != b:
                return False

    return True


def remove_grayscale(path, i):
    root, dirs, files = next(os.walk(path))

    chunk = len(files) // 8
    start = (i * chunk)
    end = ((i + 1) * chunk)

    files.sort()
    files = files[start:end]

    count = 0
    analyzed = 0
    for file in files:
        fn = os.path.join(root, file)

        if is_grayscale(fn):
            count += 1
            os.remove(fn)

        analyzed += 1
        print("Process {}, analyzed {}/{}".format(i, analyzed, len(files)))

    return count


def remove_grayscale_mp(path):
    inputs = []
    total = 0

    for i in range(8):
        inputs.append((path, i))

    with Pool(8) as p:
        results = p.starmap(remove_grayscale, inputs)

    for res in results:
        total += res

    print(total)


if __name__ == "__main__":
    path = "../../res/dataset/x/train"
    path = "../../res/dataset/y/train"

    remove_grayscale_mp(path)
