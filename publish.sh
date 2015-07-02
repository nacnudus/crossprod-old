#!/bin/bash
make publish
ghp-import output
git push origin gh-pages
