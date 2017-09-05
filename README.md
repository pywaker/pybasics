# Introduction to Python Basics Sessions
---

## Anaconda/Miniconda

Anaconda is python distribution which bundles all the required datascience tools.

> Download Anaconda from [Anaconda Website](https://www.continuum.io/downloads). Use Python 3 version.

Miniconda is smaller version of Anaconda, which contains only required packages to run anaconda.

> Download miniconda from [Miniconda website](http://conda.pydata.org/miniconda.html). Use Python 3 version.


### Installation

Linux

    > chmod +x Anaconda3-latest-Linux-x86_64.sh
    > ./Anaconda3-latest-Linux-x86_64.sh
    > nano ~/.bashrc

Mac

    > chmod +x Anaconda3-latest-MacOSX-x86_64.sh
    > ./Anaconda3-latest-MacOSX-x86_64.sh
    > nano ~/.bash_profile

Add line below to .bashrc or .bash_profile or .zshrc file

```sh 
    export PATH=$PATH:~/anaconda3/bin
```

Windows

  - Install exe file
  - update environment variable with installed Anaconda path. [See Instructions](https://www.microsoft.com/resources/documentation/windows/xp/all/proddocs/en-us/sysdm_advancd_environmnt_addchange_variable.mspx)


## Github and Git
---

- Download github desktop from [https://desktop.github.com/](https://desktop.github.com/)

### Windows

- Download git for windows from [https://git-scm.com/download/win](https://git-scm.com/download/win)

### Linux

- Install **git** from your package manager.

    **Ubuntu**
        $ sudo apt-get install git

Usage
=====

**Requires Miniconda/Anaconda to be installed**

    $ git clone https://github.com/lfapython/pybasics.git
    $ cd pybasics
    $ conda env create
    $ source activate pybasics
    $ jupyter-notebook
