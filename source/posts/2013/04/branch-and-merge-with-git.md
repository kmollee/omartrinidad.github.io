title: Git branching and merging 
date: 2013-04-25
category: Blog
tags: Git, branching, merging 

Git supports _branching_ which means that you can work on different versions of 
your collection of files in parallel. That is, it is possible create a branch 
and make the changes in this branch without affecting the state of your files in 
another branch. _The default branch is called master_.

_Branches in Git are local_. A branch created in a local repository, does not
need to have a counterpart in the remote repository.

To create a branch and switch to it at the same time, you can run the <code>git
checkout</code> command with the <code>-b</code> switch. 
    
    $ git checkout -b newbranch

This is shorthand for:

    $ git branch newbranch
    $ git checkout new branch

We are now in the branch <code>newbranch</code>. Git moved the HEAD pointer to
<code>newbranch</code>.

    $ git branch
    * newbranch
    master

_Warning:_ Before you back to your master branch, note that if your working
directory or _staging area_ has uncommitted changes that conflict with the
branch you are checking out, Git will not let you switch branches. It is best
to have a clean working state when you switch branches. 

# Merge

This section explain what is a merge.

# Delete branch

This section explain how to delete a branch.

