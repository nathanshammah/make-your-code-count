# 5 - Writing a Documentation for Your Library

## 5.1 - Comment your functions

## 5.2 - Sphinx

Use [Sphinx](http://www.sphinx-doc.org/) to generate an API documentation automatically from the comments present in the .py scripts. You can embellish the API with a User Guide, by writing some specific

Inter-Sphinx is a feature of Sphinx that creates an hypertext with functions and classes defined in other documentations. For example, you can make every instance of `np.linspace()` in your library's documentation clickable, so that a user can learn of its parameters, output and features directly on NumPy's documentation page.

## Requirements
The documentation is generated with
[Sphinx](https://www.sphinx-doc.org/en/master/usage/installation.html).
```bash
pip install -U sphinx
```
To check that Sphinx is installed you can run
```bash
pip install -U sphinx
```

## How to Build the Documentation

### Create an environment
Follow this recipe:
- Create a conda environment (here called `yourenv`) for the documentation
```bash
conda create -n yourenv
conda activate yourenv
```

### Create a branch
- Create a branch in `git` for the documentation with the release number up to
minor (e.g., Package 0.0.2---> package00X)
```bash
(yourenv) git checkout -b package00X
```

### Create the configuration file with Sphinx
- Since the documentation is already created, you need not to generate it
from scratch. If you had to generate it from scratch, the first step would
involve creating the `conf.py` file. This can be generated with a wizard
```bash
(yourenv) sphinx-quickstart
```

### Build the documentation
- To build the documentation, from `bash`, move to the `docs` folder and run
```bash
sphinx-build -b html source build
```
this should generate the `docs/build` folder. This folder is not kept track of
in the github repository, as `docs/build` is present in the `.gitignore` file.

Here above `source` and `build` are the names of the directories.

### How to modify the files

The documentation files to modify will be in the `source` folder.

The `html` and `latex`  and `pdf` files will be automatically created in the
`docs/build` folder.

- Create a structure of files in .rst or .md with the Guide. The main one
 could be called `index.rst` and similarly for other uses according to the
 purposes, for example with `guide.rst` for the guide, and `apidoc.rst` for
 the automatically generated list of functions and classes (see next).


### Automatically generate the documentation from docstrings
- Add `autodoc` to the extensions in the `conf.py` file
```bash
extensions = ['sphinx.ext.autodoc']
```
and then modify the `.rst` files giving instructions on how to parse and import
entire modules or members (functions or classes) of such modules, e.g.,
the `apidoc.rst` file could look something like
```bash
Functions
----------
.. automodule:: yourlibrary
   :members:

.. automodule:: yourlibrary.onemodule
   :members:
```
and so on.


### Generate the HTML

- To generate the `html`,
```bash
make html
```

### Generate the PDF
- To generate the `pdf`,
```bash
make latexpdf
```


## 5.3 - Use readthedocs to host online the documentation

[Read the docs](https://readthedocs.org/) allows you to host the technical
documentation of your library
for free at the website `mylibrary.readthedocs.org`.


Advance to
Section [6 - Distributing Distributing Your Library](6-distribute.md).
