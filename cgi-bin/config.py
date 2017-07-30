#!/usr/bin/python3
# -*- coding: UTF-8 -*-# enable debugging
## config.py
#
# About
#  lfs-cms configuration file
#
# Author
#  written by Clifford Bakalian and Justin Goodman
#
##

# imports
import cgi
import cgitb

cgitb.enable()

class Config:
    def __init__(self):
        # path variables
        self.URIPATH = "../"
        self.BINPATH = "../cgi-bin/"
