# Distribute


## Release the library online

- Host the library on GitHub

- List the library on `pip` or on the `conda-forge` channel in order to facilitate the installation of the package. 


## The Conda-Forge channel
Anaconda comes with a bundle of open source packages. 
It also allows the community to self mantain a "channel" for a much broader set of libraries, [Conda-Forge](https://conda-forge.org/).

As an user, all one has to do in order to install a given library hosted on conda forge is to configure the conda-forge channel to allow the download and installation of such software packages. From Terminal:

`conda config --add channels conda-forge`
`conda install <package-name>`

As a developer, there are a series of relatively simple steps that one has to follow in order to list the library on conda-forge. 

### Add a recipe
In order to host your library on conda-forge is to create a file with all the dependencies and system requirements for the given library. 
This file has a .yaml extension and can be a few lines long. See the guidelines [here](https://conda-forge.org/docs/recipe.html). 