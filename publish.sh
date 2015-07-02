#!/bin/bash
pelican content -o output -s publishconf.py
ghp-import output
git push origin gh-pages
