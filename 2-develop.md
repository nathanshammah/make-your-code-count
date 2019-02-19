# Developing your code

## Choosing a text editor
Every coder has her own favourite editor. Mine is [Sublime](https://www.sublimetext.com/3): it is crisp and favours focusing, the default dark background is relaxing, it provide appealing syntax and color rendering, it has a minimal intuitive IDE (and customizable settings). 

## Best practices in code prototyping: PEP8 in Python
Professional code developers abide to some prototyping rules. Keeping in mind that code is more read than written, these are best practices that become very useful also for non-professional developers. 
In Python, [PEP8](https://www.python.org/dev/peps/pep-0008/) is a short guide that is a suggested reading before starting to code. It includes low level rules about spacing, indentation, and so on. As well as these might look a micromanaging effort at first, they really help uniform code written by different person, avoiding that "what th heck...?!" feeling that you might have experienced at first sight when reading someone else's code. For more best practices, see the [documentation section](4-docs.md).

## Jupyter Notebooks
[Jupyter](https://jupyter.org/) is an interactive way to develop code. 

Some have gone as far as saying that [the scientific paper is obslote](https://www.theatlantic.com/science/archive/2018/04/the-scientific-paper-is-obsolete/556676/). We can certainly agree on the fact that numerical notebooks are a novel way to perform research. 
They were introduced by Wolfram Mathematica, extended in Matlab, and possibly perfected in IPython and Jupyter. 

Jupyter is simply the continuation of the IPython project (interactive Python). 

As pointed out by Guido Van Rossum, the creator of Python, Guido Van Rossum, scientific research is a trial-and-error creative approach. The faster the interactive feedback loop, the faster the distillation of ideas from code. (See it here at the [59:30 minute](https://youtu.be/ghwaIiE3Nd8?t=3528)).

Some features of the interactive notebook:

- You see the code in your browser, such as Google Chrome, Mozilla or Safari. 

- You can intersperse code with LaTeX, the prototyping choice for many researchers.  

- You can run blocks of code in the order you prefer, just like in Mathematica and MATLAB. 

- Graphics are supported in the notebook, for example with the excellent Matplotlib library. 

To install Jupyter, with conda simply run in the Terminal

`conda install jupyter`

To launch From the Terminal, go to the folder of choice and run

`jupyter notebook`


A quick way to convert .ipynb into .py files is

`$ ipython nbconvert --to=python [NOTEBOOK_NAME].ipynb` 

This can be done also inside a Jupyter notebook: 

`!ipython nbconvert --to=python config_template.ipynb`
