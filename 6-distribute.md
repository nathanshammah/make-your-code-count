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

You can use [`twine`](https://pypi.org/project/twine/) to register and upload the library. From the Terminal:

```
pip install twine
```
Then go to your library folder, such as `mylibrary/` here, and type

```
python setup.py sdist bdist_wheel
```

which builds a local version ready to be shipped to PyPI.

Register on [Test PyPI](https://packaging.python.org/guides/using-testpypi/) website. Once you are registered, test with an upload on Test PyPI, so that you will not directly affect PyPI,

```
twine upload --repository-url https://test.pypi.org/legacy/ dist/*
```

You will find your package at the URL
[https://test.pypi.org/project/<package>](https://test.pypi.org/project/<packaget>), where `<package>` is replaced by the name of the library package, in this tutorial `mylibrary`.

[https://packaging.python.org/guides/using-testpypi/](https://packaging.python.org/guides/using-testpypi/)


[https://hynek.me/articles/sharing-your-labor-of-love-pypi-quick-and-dirty/](https://hynek.me/articles/sharing-your-labor-of-love-pypi-quick-and-dirty/)

[https://caremad.io/posts/2013/07/setup-vs-requirement/](https://caremad.io/posts/2013/07/setup-vs-requirement/)

## 6.3 - The Conda-Forge channel
Anaconda comes with a bundle of open source packages.
It also allows the community to self maintain a "channel" for a much broader set of libraries, [Conda-Forge](https://conda-forge.org/).

As an user, all one has to do in order to install a given library hosted on conda forge is to configure the conda-forge channel to allow the download and installation of such software packages. From Terminal:

`conda config --add channels conda-forge`
`conda install <package-name>`

As a developer, there are a series of relatively simple steps that one has to follow in order to list the library on conda-forge.

### 6.4 - Add a recipe
In order to host your library on conda-forge is to create a file with all the dependencies and system requirements for the given library.
This file has a .yaml extension and can be a few lines long. See the guidelines [here](https://conda-forge.org/docs/recipe.html).


Advance to Section [7 - Publishing Your Results](7-publish.md).
