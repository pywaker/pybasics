Pybasics Introduction
=====================

# Anaconda/Miniconda
---

## Downloading Miniconda/Anaconda

Anaconda is python distribution which bundles all the required datascience tools.

> Download Anaconda from [Anaconda Website](https://www.continuum.io/downloads). Use Python 3 version.

Miniconda is smaller version of Anaconda, which contains only required packages to run anaconda.

> Download miniconda from [Miniconda website](http://conda.pydata.org/miniconda.html). Use Python 3 version.


## Installation
---


Windows

  - Install exe file
  - update environment variable with installed miniconda path. [See Instructions](https://www.microsoft.com/resources/documentation/windows/xp/all/proddocs/en-us/sysdm_advancd_environmnt_addchange_variable.mspx)

Linux

    > chmod +x Miniconda3-latest-Linux-x86_64.sh
    > ./Miniconda3-latest-Linux-x86_64.sh
    > nano ~/.bashrc

Mac

    > chmod +x Miniconda3-latest-MacOSX-x86_64.sh
    > ./Miniconda3-latest-MacOSX-x86_64.sh
    > nano ~/.bash_profile

Add line below to .bashrc or .bash_profile or .zshrc file

```sh 
    export PATH=$PATH:~/miniconda3/bin
```

Usage
=====

**Requires Miniconda/Anaconda to be installed**

    $ git clone https://github.com/lfapython/pybasics.git
    $ cd pybasics
    $ conda env create
    $ source activate pybasics
    $ jupyter-notebook
