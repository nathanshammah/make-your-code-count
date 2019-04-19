# 6 - Distributing Your Library


## 6.1 - Release the library online

- Host the library on GitHub

- List the library on `pip` or on the `conda-forge` channel in order to facilitate the installation of the package. 


## 6.2 - Python Package Index (PyPI)

It is possible to host your library, e.g., `mylibrary`, onto the Python Package Index (PyPI). This will allow everyone to install it simply with the command

```
pip install mylibrary
```

A detailed guide is present on Real Python, [How to Publish an Open-Source Python Package to PyPI](https://realpython.com/pypi-publish-python-package/).

## 6.3 - The Conda-Forge channel
Anaconda comes with a bundle of open source packages. 
It also allows the community to self mantain a "channel" for a much broader set of libraries, [Conda-Forge](https://conda-forge.org/).

As an user, all one has to do in order to install a given library hosted on conda forge is to configure the conda-forge channel to allow the download and installation of such software packages. From Terminal:

`conda config --add channels conda-forge`
`conda install <package-name>`

As a developer, there are a series of relatively simple steps that one has to follow in order to list the library on conda-forge. 

### 6.4 - Add a recipe
In order to host your library on conda-forge is to create a file with all the dependencies and system requirements for the given library. 
This file has a .yaml extension and can be a few lines long. See the guidelines [here](https://conda-forge.org/docs/recipe.html). 


Advance to Section [7 - Publishing Your Results](7-publish.md).
