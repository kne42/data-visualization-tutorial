# Data Visualization Tutorial

> SciPy 2018 Conference

> AT&T Conference Center at Austin, Texas

> Presented by Kira Evans and David Shupe

[![Travis Status](https://travis-ci.org/kne42/data-visualization-tutorial.svg?branch=master)](https://travis-ci.org/kne42/data-visualization-tutorial)
[![Appveyor Status](https://ci.appveyor.com/api/projects/status/0q90ktvb2n3oxee1/branch/master?svg=true)](https://ci.appveyor.com/project/kne42/data-visualization-tutorial/branch/master)

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
$ conda env create -f environment.yml
```

If you're on MacOS or Linux, activate the environment with:
```bash
$ source activate dv-tut
```

Or the following if on Windows:
```bash
$ activate dv-tut
```

## Jupyter Magic!

Start a jupyter notebook with the following:
```bash
$ jupyter notebook 00-overview.ipynb
```
