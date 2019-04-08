# Hosting


You might find it useful to have some tools for an online interactive classroom using your library. Online notebooks can be run with [My Binder](https://mybinder.readthedocs.io/en/latest/index.html), while setting up more persistent features could be desirable during educational activities such as workshops and classroom coursework.

There has been quite some development in the Project Jupyter community toward this end, which led to [JupyterHub](https://jupyterhub.readthedocs.io/en/latest/index.html) and more recently to [BinderHub](https://binderhub.readthedocs.io/en/latest/), an overlay of JupyterHub focused on notebook hosting.

For the server there are mainly two options:

- Setting up your own (institutional) server to do this, which would require initially more time and commitment (you need to worry about the security of the network, to start);

- Using cloud services (such as Google Cloud), which might be easier at first but can quickly become too expensive if you have a large user community. 

There are now a couple of [guides](https://zero-to-jupyterhub.readthedocs.io/en/latest/) to deploy JupyterHub, such as the [The Littlest JupyterHub](https://github.com/jupyterhub/the-littlest-jupyterhub).

For the services, there are possibly two features for the community:

- Set-up of a cloud service for library-based workshops, which can be used temporarily by instructors and students / participants.

- Set-up of a continuously running cloud service for the library users community.

Features allowing to flesh out your library live could be also implemented in a website with a live interface, such as for [live.sympy.org](https://live.sympy.org/), built upon Google App Engine, or the similar project Sympy Gamma. 

## Run notebooks interactively on the cloud with My Binder
[My Binder](https://mybinder.readthedocs.io/en/latest/introduction.html#what-is-the-binder-project)
allows to run Jupyter Notebooks interactively from the cloud.
Anyone will be able to run notebooks from your repository, simply with an Internet connection, by clicking on the `binder` icon.
All you need to do to make `binder` active is:
 
 - Create a file specifying the notebook requirements in the notebooks folder, say `mylibrary/notebooks`. The requirements will likely be equale to the library requirements. This can be a `requirements.txt` using `pip` as default package manager, or a `environment.yml` file if you wish to use `conda` as package manager (you can also specify to use `pip` in the `environment.yml` file). If you use LaTeX, including a text file `apt.txt` allows you to plot with your [typographic preferences](https://github.com/binder-examples/latex).  

 - Go to [https://mybinder.org/](https://mybinder.org/), paste the name of the repository where the notebooks are collected, say `mylibrary/notebooks`. My Binder will generate a link thayou can embed in the Readme.MD file on Github or in other places. Clicking this link will activate My Binder, which will install the dependencies and library according to the requirements file.

## Host on JupyterHub
If you would like your software capabilities to be used by a delocalized team, without even requiring someone to download the software of install it, this can be done with [JupyterHub](https://github.com/jupyterhub/jupyterhub) as well as private services offered by some startups. 
JupyterHub and BinderHub allow to run notebooks interactively, also setting up specific servers
(as a machine at a research institution) or using online cloud services (such as Google and AWS). 