# Publishing


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

## Publish peer-reviewed research papers that use the library 
This is probably the standard output that scientists as physicists have been aiming at even before the advent of open-source software development. 
This is still one of the main markers in academic activity. 

## Publish the library and dataset on Zenodo
[Zenodo](https://zenodo.org/) is a service that allows to publish code, a dataset or a full-fledged library, on an online repository that anyone can access. 
Zenodo was a project started at CERN with the backing of the European Union and now its use fall perfectly in line with open data policies, such OpenAIRE and EOSC.

You can set up Zenodo with a switch directly from the GitHub page of your repository. 

Zenodo offers a two-fold opportunity:

For the researchers who developed the code, it provides instantaneously a DOI reference. 
The arXiv currently does not provide such bibliographic identifier. 
This is useful to protect claims of a discovery or research idea, as a code might not end up in a research paper. 

For the research community and especially for referees of a paper related to the library and/or dataset, it provides a crystallization of the version release.
This can help check that a given tool does what it claimed to do at the time of submission. 
In this way, reproducibility of results is made easiers. 

## Present the library in a peer-reviewed research paper
There are now multiple oultlets that are tailored to present software packages that are related to research. 
A classic one is Computer Physics Communications. 

In physics and quantum physics in particular there are several alternative options (for more details on open-source libraries in quantum technology, see 
"The rise of open source in quantum physics research" [blog post](http://blogs.nature.com/onyourwavelength/2019/01/09/the-rise-of-open-source-in-quantum-physics-research/).
):

- [SciPost](https://scipost.org/) journals such as SciPost Physics, which cover all physics, with a focus on condensed-matter applications. 
The papers of the QuSpin library have been published there. 

- [Quantum](https://quantum-journal.org/), a community-driven journal that has already published papers on the ProjectQ and other quantum tech projects. 

- PLOS One, which ran a special issue focusing on quantum software.  

## Run notebooks interactively on the cloud with My Binder
[My Binder](https://mybinder.readthedocs.io/en/latest/introduction.html#what-is-the-binder-project)
allows to run Jupyter Notebooks interactively from the cloud.
Anyone will be able to run notebooks from your repository, simply with an Internet connection, by clicking on the `binder` icon.
All you need to do to make `binder` active is:
 
 - Create a file specifying the notebook requirements in the notebooks folder, say `mylibrary/notebooks`. The requirements will likely be equale to the library requirements. This can be a `requirements.txt` using `pip` as default package manager, or a `environment.yaml` file if you wish to use `conda` as package manager (you can also specify to use `pip` in the `environment.yaml` file).

 - Go to [https://mybinder.org/](https://mybinder.org/), paste the name of the repository where the notebooks are collected, say `mylibrary/notebooks`. My Binder will generate a link thayou can embed in the Readme.MD file on Github or in other places. Clicking this link will activate My Binder, which will install the dependencies and library according to the requirements file.

## Host on JupyterHub
If you would like your software capabilities to be used by a delocalized team, without even requiring someone to download the software of install it, this can be done with [JupyterHub](https://github.com/jupyterhub/jupyterhub) as well as private services offered by some startups. 
JupyterHub and BinderHub allow to run notebooks interactively, also setting up specific servers
(as a machine at a research institution) or using online cloud services (such as Google and AWS). 

## Useful Links
- [Installing Python Packages from a Jupyter Notebook](https://jakevdp.github.io/blog/2017/12/05/installing-python-packages-from-jupyter/)
 
- [The Littlest JupyterHub](https://github.com/jupyterhub/the-littlest-jupyterhub)

- [My Binder Documentation](https://mybinder.readthedocs.io/en/latest/index.html)

- [Zero to JupyterHub](https://zero-to-jupyterhub.readthedocs.io/en/latest/index.html)

- [BinderHub Documentation (project in development)](https://binderhub.readthedocs.io/en/latest/)
