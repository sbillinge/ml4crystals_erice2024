# Set up git and terminals on your computer

To begin with we will work terminals that have the program `git` installed.  If you have MacOS or Linux you are already in good shape, just open a terminal and it should work.
If you are working on windows, we recommend installing and using [Git For Windows](https://gitforwindows.org/) which gives you a unix-style `bash` terminal with git already installed.

If you are not familiar with using a terminal, spend a bit of time reading about using unix terminals to get comfortable.

# Getting the course materials

You will find the course materials on GitHub at the link given in the course materials.  

We will first download the materials from there. In this course we will spend some time to get used to using git and GitHub, something that you may find very useful in all your coding work (your GitHub history can also help you get a job so try and maintain a somewhat professional image there.  Treat it like LinkedIn rather than Tiktok...).
For now, follow these instructions.
1. Open a terminal 
2. Navigate to where you keep you want to work, e.g., type `mkdir ml4ms-course` to make an empty directory for your coursework, then `cd ml4ms-course` to move there.
   - Recommendations for working with terminals:
      - Never use any folder names with spaces in them (or non ascii characters for that matter)
      - Never let your operating system (i.e., Windows Explorer or Finder on Mac) be in charge of where to save files.
      - In a terminal it is really easy to go to you your "home" directory by typing `cd ~`.  This is usually the default directory you find yourself in when you open a new terminal.
      - Therefore...build all your working directories off your home directory, making them very easy to find from the terminal
1. Go to the course GitHub repository page in your browser
2. Make a fork of the repo in your own GitHub account: click the `Fork` button and follow the instructions.
3. Make a local 'clone' of your fork on your computer:
   1. Find your fork of the course GitHub page in your browser
   1. Click on the green "Code" button.  If you are familiar with git and GitHub then clone the repo.  If not, we will cover this in class, but for now download the zip file and unpack it.
4. Open the README.md file (this file) and follow the instructions

# Virtual environments and Conda

In python programming, we often use many python packages in conjunction to write codes. However, it can be hard to manage the different python packages since they all have different versions and dependencies. Furthermore, different pieces of codes could require different versions of the same package. As you can guess, package management becomes messy very easily. 

To get around this the concepts of virtual environments was invented.  The idea is that your "environment" is your computer operating system.  It knows about what is installed on your OS and it doesn't know anything else.  You can update your environment to know about more things by installing new apps and programs.  So let's extend this concept to a "virtual environment" that is a kind of sub-environment on your OS that only knows about what is in that environment.  The steps are then:
1. create a virtual environment and give it a name
2. install things in it
3. when you want to use it, activate the environment so your current session/process is living in that environment
4. use it
5. when you are done, deactivate it

This is very powerful because I can create an env to run a particular program, and another env to run a different program that has incompatible needs, and I can run them both on my OS because they live in separate environments.

__recommendation__: starting now, do all your python work using virtual environments.  Never don't use them.

We need some software to manage our virtual environments.  At the time of writing we like to use miniconda with mamba.

Miniconda is a software that makes installing and managing python packages much simpler. The user can create multiple "conda environments". Each conda environment keeps a library of packages and makes sure that each package's version is compatible with every other package in the environment. You can pick which environment to use when running different coding projects which require different combinations of the packages and their versions. 

For uniformity and easier debugging, we will require everyone to use miniconda for the edexes in the course. 

Miniconda is a package manager produced by the company Continuum, which also has a number of other "products".  It is easy to mix up "conda", "Anaconda", "miniconda" and "conda-forge". Here are the differences. The Anaconda distribution comes from Continuum pre-loaded with many commonly used packages while the miniconda distribution is just the management system without any pre-loaded packages. `conda` is the software underlying Anaconda and Miniconda. "conda-forge" is a community supported "channel" in conda where people share their software packages.  We like this platform because it is good at handling interdependencies of packages.  It also provides you with pre-compiled packages that should work uniformly across different platforms.  At the time of writing it is strongly preferred that you use it.  The package dependency task is complicated and conda can get slow resolving all the dependencies when there are many of them.  There is a new faster version of the `conda` management software called `mamba` that works very nicely in the same conda ecosystem, so we strongly recommend this also.  Mamba is designed to work with conda-forge.  Below we give the steps to install the "stack" in the way we would like you to do this for this class.  

We believe that this is a good way to set up your computer and if you learn these things now, it will be a gift that keeps on giving as you move forward.

### Install and set up miniconda and mamba

Installing miniconda is pretty straightforward. Go to the links below and select the graphical installer based on your operating system:

[miniconda](https://docs.conda.io/en/main/miniconda.html)

- Open a terminal on you computer.
- See what envs you have on your computer type: `conda info --envs`.  If you just installed miniconda you will only see a `base` env.
- Next we want to ask conda to always look first in the `conda-forge` channel for packages by default: `conda config --add channels conda-forge`
- We will install mamba in our base environment: `conda install mamba`. (select y to approve the installation)
- Next we want to update our `base` and make it compatible with `mamba`.  Type: `mamba update --all`.  This updates all the packages in your base to the latest `conda-forge` versions of those packages. 
- We will also want to use Jupyter from many of our environments, so let's also install that in the base environment: `mamba install jupyter`

Later you will create and then activate environments.  The environments are separate from each other (that is the point) _except_ the base environment.  

All the other environments inherit what is in the `base` environment so work hard to keep your `base` clean.  _only install `conda`, `mamba` and `jupyter` in your base __and nothing else__._    If you accidentally install other things in base, don't worry too much.  You can remove them if you need to, or if your base gets very dirty, it is quite quick to reinstall a clean miniconda (using the steps laid out above) and rebuild your envs.  It is good practice to do this from time to time anyway.  It can actually save quite a bit of frustrating debug time when things get dirty.

With this setup done, you should be able to open a new terminal window and simply type `jupyter notebook` or `jupyter lab` in the terminal to open a jupyter session in your browser.  _It is recommended to navigate to your working folder-tree (i.e., using `cd`) in the terminal before typing `jupyter notebook`._

Now you can close this README, open a new terminal, navigate to the folder where your course materials were downloaded from GitHub, type `jupyter notebook`, then in the browser navigate to find the `virtual_environment_setup.ipynb` notebook and open it.  The beginning part of that notebook repeats what is in this README.  Look for the section heading __Continued from Readme.md__ in that notebook and continue from there.

Here are more detailed instructions in case you need them (and want to refer back later)
- make sure you are in the file folder on your hard-drive where these files are
- with your `ml4ms-skl` env activated, type: `jupyter notebook`
- wait for the program to run, then go to your browser and look for a tab that has jupyter running in it.  
- you should see a list of files and folders.  You just have to navigate to and double-click the `virtual_environment_setup.ipynb` file and it will open in a tab in your browser.
- you should see more or less exactly what is in this readme, repeated there for good measure
- If you are not familiar with jupyter, do some reading about it to get used to it

Jupyter uses a web browser as an IDE (interactive development environment...we used to call them editors in the old days).  This is very convenient and gets you going very quickly.  The more coding you do though, the more you will benefit from a full featured IDE like PyCharm or VScode.  Since these run jupyter these days, you can have your cake and eat it and install the IDE and still work with jupyter (this is how Simon does it).
It is not required for the course, but if you would like to now, or later, it is a definite recommendation for working faster.
Simon likes using PyCharm, and as a student you can have a free educational license for the full professional version and be like a professional programmer.  Go to the [PyCharm website](https://www.jetbrains.com/pycharm/) and download and install the professional version, register yourself as a student.
