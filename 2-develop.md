# Developing your code


## Jupyter Notebooks
[Jupyter](https://jupyter.org/) is an interactive way to develop code. 

Some have gone as far as saying that [the scientific paper is obslote](https://www.theatlantic.com/science/archive/2018/04/the-scientific-paper-is-obsolete/556676/). We can certainly agree on the fact that numerical notebooks are a novel way to perform research. 
They were introduced by Wolfram Mathematica, extended in Matlab, and possibly perfected in IPython and Jupyter. 

Jupyter is simply the continuation of the IPython project (interactive Python). 

As pointed out by Guido Van Rossum, the creator of Python, Guido Van Rossum, scientific research is a trial-and-error creative approach. The faster the interactive feedback loop, the faster the distillation of ideas from code. (See it here at the [59:30 minute](https://youtu.be/ghwaIiE3Nd8?t=3528)).

Some features of the interactive notebook:

- You see the code in your browser, such as Google Chrome, Mozilla or Safari. 

- You can intersperse code with LaTeX, the prototyping choice for many researchers.  

- You can run blocks of code in the order you prefer, just like in Mathematica and Matlab. 

- Graphics are supported in the notebook, for example with the excellent Matplotlib library. 

To install Jupyter, with conda simply run in the Terminal

`conda install jupyter`

To launch From the Terminal, go to the folder of choice and run

`jupyter notebook`


A quick way to convert .ipynb into .py files is

`$ ipython nbconvert --to=python [NOTEBOOK_NAME].ipynb` 

This can be done also inside a Jupyter notebook: 

`!ipython nbconvert --to=python config_template.ipynb`
