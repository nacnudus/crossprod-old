# Crossprod

## Python/virtualenv

Before you do anything, do `workon crossprod`, which will put you in the correct
python environment and the /home/nacnudus/crossprod directory.

## Writing posts

* Commit drafts to their own branch first (not `drafts`, in case you don't want
  to publish them in order), then merge into master.  
* Name all chunks, otherwise the automatically-named
  cache and figure files of different posts will overwrite one another.
* Load packages in their own chunk (can't be cached).

## (Re)generating the site

* `make html` regenerates the site
* `make serve` serves it locally at http://localhost:8000/
* `make devserver` serves it locally, and regenerates it when posts are edited.
  `make stopserver` in another terminal will allow you to cancel the process
  with `ctrl+c`.
* `make publish` *doesn't* publish, rather makes it as though it were
  publishing, using the `publishconf.py` script.
* `make github` publishes to GitHub, available at https://nacnudus.github.io/crossprod/
* Read the Makefile for other `make` commands

## Viewing the site

Use http, not https, or the Disqus comments won't load.
