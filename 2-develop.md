# 2 - Developing Your Code

## 2.1 - Best practices in code prototyping: PEP 8 and PEP 257
Professional code developers abide to some prototyping rules. Keeping in mind that code is more read than written, these are best practices that become very useful also for non-professional developers. 
In Python, [PEP 8](https://www.python.org/dev/peps/pep-0008/) is a short guide that is a suggested reading before starting to code. It includes low level rules about spacing, indentation, and so on. As well as these might look a micromanaging effort at first, they really help uniform code written by different person, avoiding that "what th heck...?!" feeling that you might have experienced at first sight when reading someone else's code. 

Similarly to PEP 8 for code, [PEP 257](https://www.python.org/dev/peps/pep-0257/) provides best practices for docstrings, the comments accompanying functions and classes in Python. These are especially relevant as they will be used by specific software, such as Sphinx, to automatically build the documentation, see the [Documentation section](4-docs.md).

## 2.2 - Jupyter notebooks
[Jupyter](https://jupyter.org/) is an interactive way to develop code. 

Some have gone as far as saying that [the scientific paper is obsolete](https://www.theatlantic.com/science/archive/2018/04/the-scientific-paper-is-obsolete/556676/). We can certainly agree on the fact that notebooks are a novel way to perform research and present it to others.
They were introduced by Wolfram Mathematica, extended in Matlab, and possibly perfected in IPython and Jupyter. 

Jupyter is simply the continuation of the IPython project (Interactive Python). 

As pointed out by Guido Van Rossum, the creator of Python, scientific research is a trial-and-error creative approach. The faster the interactive feedback loop, the faster the distillation of ideas from code. (See it here at the [59:30 minute](https://youtu.be/ghwaIiE3Nd8?t=3528)).

Some features of the interactive notebook:

- You see the code in your browser, such as Google Chrome, Mozilla or Safari. 

- You can intersperse code with LaTeX, the prototyping choice for many researchers.  

- You can run blocks of code in the order you prefer, just like in Mathematica and MATLAB. 

- Graphics are supported in the notebook, for example with the excellent Matplotlib library. 

To install Jupyter, with conda simply run the following in the terminal

`conda install jupyter`

To launch from the terminal, go to the folder of choice and run

`jupyter notebook`

More information about how to host Jupyter notebooks on the cloud are given in [Section 7](7-host.md).

## 2.3 - Converting Jupyter notebooks in .py scripts

A quick way to convert .ipynb into .py files is

`$ ipython nbconvert --to=python [NOTEBOOK_NAME].ipynb` 

This can be done also inside a Jupyter notebook: 

`!ipython nbconvert --to=python config_template.ipynb`


Advance to Section [3 - Testing your code](3-test.md)
