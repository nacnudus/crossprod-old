# OPRE

## Python/virtualenv

Before you do anything, do `workon opre`, which will put you in the correct
python environment and the /home/nacnudus/opre directory.

## Writing posts

* Commit drafts to the `drafts` branch first, then merge into master.
* Always name chunks that produce figures, otherwise the automatically-named
  figure files of different posts will overwrite one another.

## (Re)generating the site

* `make html` regenerates the site
* `make serve` serves it locally at http://localhost:8000/
* `make devserver` serves it locally, and regenerates it when posts are edited.
  `make stopserver` in another terminal will allow you to cancel the process
  with `ctrl+c`.
* `make publish` publishes to GitHub, available at https://nacnudus.github.io/opre/
* Read the Makefile for other `make` commands

