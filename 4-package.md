# 4 - Packaging your Library
Here you will learn how to elevate your code from a file or collection of files to a proper library.

## 4.1 -  Installing the library locally
Inside a `setup.py` file you save all the information about setting up your library.
[Minimal guide to packaging](https://python-packaging.readthedocs.io/en/latest/minimal.html).
The hitchhiker's guide to packaging is also a [minimal guide](https://the-hitchhikers-guide-to-packaging.readthedocs.io/en/latest/quickstart.html) to follow all the steps. Once completed, running from the `mylibrary` folder

```
python setup mylibrary
```
which will magically install the library, such that then you will not need to be in the same folder of `mylibrary.py` to import functions and classes there defined. You will treat it on par with other libraries, such as Numpy, Scipy or scikit-learn, invoking it simply with

```
from mylibrary import *
```

which will allow you to run its function simply as

```
hello()
```

In a technically more correct way, you could import the library with an alias,


```
import mylibrary as ml


ml.hello()
```

as a best practice to avoid conflicts with functions or classes that share the same name.

## 4.3 -  Develop mode
During the elaboration of your project, you might want to try things out and keep developing your library. In this case, the way to go more easily is to use the command
```
python develop mylibrary
```
which makes it more agile.


Advance to Section [5 - Writing a Documentation for Your Code](5-docs.md).
