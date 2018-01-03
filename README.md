## Setup Instructions

Clone the tutorial repository and change your working directory:
```bash
$ git clone https://github.com/kne42/data-visualization-tutorial.git
$ cd data-visualization-tutorial
```

If you do not have `git` installed, you can
[download the tutorial as a zip](https://github.com/kne42/data-visualization-tutorial/archive/master.zip).


## Install Conda

[![Install Conda](./res/conda_logo.svg)](https://conda.io/miniconda)

If you haven't already, install [conda](https://conda.io/miniconda).

## Anaconda as a Setup Tool

Create a new environment with the right dependencies:
```
$ conda create -n data-visualization-tutorial --file=spec.txt -y
```

If you're on MacOS or Linux, activate the environment with:
```bash
$ source activate data-visualization-tutorial
```

Or the following if on Windows:
```bash
$ activate data-visualization-tutorial
```

## Activating Jupyter Notebook

Start up a notebook pointing to the index:
```bash
$ jupyter notebook 00-overview.ipynb
```
