import splitfolders

if __name__ == "__main__":
    seed = 42
    input_folder = '../../res/dataset/y/'
    output_folder = '../../res/dataset/y/splitted/'
    ratio = (0.8, 0.1, 0.1)

    splitfolders.ratio(input_folder, output=output_folder, seed=seed, ratio=ratio, group_prefix=None)
