# 1 - Manage a Code Project

## 1.1 - Choosing a text editor
Every coder has her own favourite editor. Mine is [Sublime](https://www.sublimetext.com/3): it is crisp and favours focusing, the default dark background is relaxing, it provide appealing syntax and color rendering, it has a minimal intuitive IDE (and customizable settings). 

## 1.2 - Version Control with Git
There is no escape: for modern collaborative projects, the way to go is to make an effort and learn some basic tools of version control, which means using `git` and Github (or a similar provider). The effort of this steep learning curve will be rewarded as the complexity of your project increases. 

### 1.2.1 - Syncing git
Sync GitHub with your computer using `git`: 
- [Create a repository on GitHub](https://help.github.com/articles/adding-an-existing-project-to-github-using-the-command-line/) and then add sync it with your machine.  

### 1.2.2 - Using git
There are a few basic concepts to start using git, and they involve some jargon, as for GitHub. 

`git init`: Move to a given folder from the Terminal, such as `cd Dropbox/dev/` and tell `git` that this folder needs to be initialized. 

`git status`: Check the status of your folder with respect to the origin (which is the folder on GitHub). You can always set what is your [remote](https://help.github.com/articles/adding-a-remote/) repository locally.  

`git add .`: After you have made your changes to the files of your folder (repository) on your machine, you want to add all this changes to the modification you want to submit (commit). 

`git commit -m "your comment"`: you are submitting a modification in a bundle (commit) and you are commenting the modification for your records (a track of this changes will be available in the repository history). 

`git pull`: this command downloads the current version of the repository (master or branch) to your local machine, e.g. with `git pull origin master`;

`git push <branch>`: this command uploads the current version of your local repository to the online copy, e.g. with `git push origin master`;

`git checkout -b <new-branch>`: Create a new branch; moving from the `master` to a brandch is equivalent to taking a diversion from the main route, in order to do some changes without affecting the core project, at least yet. 

`git merge <branch>`: Once you are satisfied with the changes, you are ready to merge the branch back into the master and eventually you can delete the branch. 


## 1.3 - Using GitHub (or a similar provider)
GitHub provides the largest collection of code projects in the world. This is an invaluable treasure of searcheable open-source projects from which you can copy, modify, and get inspiration for your own library and benefit as a simple user. As of 2019, Github allows single users also to host private repositories for free. GitHub has been acquired in late 2018 by Microsoft. Other similar services include [Gitlab](https://about.gitlab.com/) and [BitBucket](https://bitbucket.org/).
