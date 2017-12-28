X.509 CA helpers
================

This project provides an easy structure of Python classes and functions to
describe a tree of certificate authorities and certificates as its leafs. This
is useful to quickly generate testing infrastructure with root CAs that can be
installed in common browsers. The end result is a Python script that uses this
library that creates a tree of files and folders in a destination folder
representing the described infrastructure.

To implement this in such a way that it can be later extended using openssl,
this project relies on invoking the `openssl` command-line binary with a number
of provided configuration templates.

My personal use-case is to generate unique CAs and certificates for my personal 
`salt configuration <https://github.com/jdelic/saltshaker>`__.

`# TODO: fill this with actual examples once the code is written ;)` 
