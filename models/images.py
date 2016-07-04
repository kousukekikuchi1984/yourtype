# -*- coding: utf-8 -*-

import sys, re, os

from bs4 import BeautifulSoup


class ImageOp(object):

    def __init__(self):
        self.dir = 'gensun.org'
        target_re = re.compile(r'female.html|female_\d.html', re.M)
        files = os.listdir(self.dir)
        #
        self.targets = []
        for f in files:
            if re.search(target_re, f):
                self.targets.append(f)

