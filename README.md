# CycleGAN
You can read the project explaination here: 
https://docs.google.com/document/d/1Eeq1lYp01QimSYfL7lo4ydQUKEBfPuumDcpRwTnM77E/edit?usp=sharing

# Deployment and run
## Dependencies
Run
```
conda env create -f environment.yml
```
to install the needed dependencies.

Then, activate the environment:
`conda activate gan`

After that, install additional dependencies using:
`pip install flickrapi IPython opencv-python tensorflow-addons split-folders`

## Checkpoint
Create the directory first using `mkdir -p res/checkpoints/train/`.

Download the weights (link in relation) and place them in the following folder: `res/checkpoints/train/`. 

## Datasets
Create the directory first using `mkdir -p res/dataset/x/` and `mkdir -p res/dataset/y/`.

Download the datasets (link in relation) and place them in order to have the following structure 
(create the train/test/val directories first, like before):
- portrait task: `res/dataset/x/train/image0.jpg` and `res/dataset/y/train/image0.jpg`
- flower task: `res/dataset/x/train/jpg/image0.jpg` and `res/dataset/y/train/jpg/image0.jpg`

Note that the flower task needs a `jpg/` additional folder.

You can manually divide the datasets into train/test/val or use the script in `utils/splitter.py`

## Run
Run the `notebook.ipynb` using `jupyter notebook` command.

# Other scripts
The documentation of other (less important) scripts is a work in progress.
