---
layout: post
title:  "An Inaccurate Description of GIT"
date:   2022-06-14 09:59:00 +0200
categories: tech
---

What is GIT?
In essense GIT is a giant acyclic graph, each commit references its parent and 'master' is the main branch


GIT is made of three types of objects:
- Commit: Author, Message and Pointer to a 'Tree' of Changes
- Tree: Pointer(s) to file names, content other trees
- Blob: Data
- Tags and Branches: Pointers to Commits (Not copies), Can be used to name a commit and add other meta data

'HEAD' is a special pointer to the latest commit on a branch
Every branch has a HEAD pointer attached to it.

GIT is basically a table of references and references need to be unique. Therefore we use 40 character SHA1 hashes that is based on the content. Therefore a repetiation is the hash is unlikely.

The objects are organized into folders based on the first two characters.

git init creates a template of files under .git these have for example references to the HEAD

As soon as a file is created or edited a SHA object is created with the content/changes and a refernce is store in an index.

When you commit a change, a commit object is created with references to the all the trees related to that commit which in turn has a reference to all the changes. Git therefore has a reference to the file as a hash for every version of the file at each commit point.

Even a branch is just a reference to a commit. Subsequent commits on that branch are then based on that particular commit.
