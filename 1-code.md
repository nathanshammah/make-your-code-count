# 1 - Managing a Code Project

## 1.1 - Using the Terminal
In order to use `Git` and easily navigate through folder (repositories), you can use the Terminal. The default shell takes Bash commands. 


## 1.2 - Choosing a text editor
Every coder has her own favourite editor. A popular choice is [Sublime](https://www.sublimetext.com/3): it is crisp and favours focusing, the default dark background is relaxing, it provide appealing syntax and color rendering, it has a minimal intuitive IDE (and customizable settings). You can launch [Sublime from the command line](https://olivierlacan.com/posts/launch-sublime-text-3-from-the-command-line/). In the Terminal, navigate to the folder of your choice and open its contents with

```
subl . 
```

## 1.2 - Version Control with Git
There is no escape: for modern collaborative projects, the way to go is to make an effort and learn some basic tools of version control, which means using `git` and Github (or a similar provider). The effort of this steep learning curve will be rewarded as the complexity of your project increases. 

### 1.2.1 - Syncing git
Sync GitHub with your computer using `git`: 
- [Create a repository on GitHub](https://help.github.com/articles/adding-an-existing-project-to-github-using-the-command-line/) and then sync it with your machine.  

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

The basics of GitHub is that to contribute to an open-source projects there are three connected locations. Roughly speaking: 

- the "official" online repository of the project (your `upstream`);

- the copy of such repository on your profile (your `origin`);

- the local copy of your repository on your machine. 

A typical workflow would consist in the synchronization and update with modifications of these three different locations where the code project lives. 

### 1.3.1 - Create a Repository
To create a new repository from scratch, you can navigate to your GitHub account profile page, select **Repositories** from the tabs and then click on **New**. Github will guide you through the creation of a new repository online.   

### 1.3.2 - Fork Someone Else's Repository
In order to contribute to an existing open-source project, once you have your GitHub account, navigate to the repository of your choice and click on the upper right on **Fork**. This command creates a copy of the project's folder on your profile. 

### 1.3.3 - Clone a Repository
In order to create the local copy of one of your profile's repository, hosted online on GitHub, such as `mylibrary`, you can clone it. On the upper right part of the web page, click on **Clone or download** and copy the link that appears. Then, on your machine, open the Terminal, navigate to the folder where you wish to keep this repository (such a `github/` folder), and then write in the terminal 

```
git clone https://github.com/yourusername/mylibrary.git
```   

### 1.3.4 - Contribute to a project: Open a Pull Request
To open a pull request (PR), navigate to the repository webpage, such as QuTiP's [`qutip/qutip`](https://github.com/qutip/qutip), click on the right menu where you can find an [**Pull Requests**](https://github.com/qutip/qutip/pulls) tab. 
You can click on **New pull request** to raise a PR online, however the best practice is usually to go through your fork and open it from your remote origin repository. 

### 1.3.5 - Contribute to a project: Raise an Issue
To raise an issue, navigate to the repository webpage, such as QuTiP's [`qutip/qutip`](https://github.com/qutip/qutip), click on the right menu where you can find an [**Issues**](https://github.com/qutip/qutip/issues) tab, and then click on **New issue**. There are some best practices on starting new issues. Some are project-independent, some are project specifics. For example, in repository where you have administrative rights, you can improve the issue traceability by adding some metadata, such as giving the issue a label, or asking for a specific user to look into it. 

Although the word "Issue" sounds quite negative, Issues can be brought up also regarding enhancements to a project. Once an issue is taken care of, it can be closed.  All closed issues are listed on a repository's page on Github. 

## 1.4 - Useful Links
- [Add Sublime to the command line](https://olivierlacan.com/posts/launch-sublime-text-3-from-the-command-line/)
- [GitHub: Add remote repo](https://help.github.com/articles/adding-a-remote/).
- [GitHub: Create a repository](https://help.github.com/articles/adding-an-existing-project-to-github-using-the-command-line/)


Advance to Section [2 - Developing Your Code](2-develop.md).
