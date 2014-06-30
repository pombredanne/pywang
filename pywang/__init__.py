#!/bin/env python
# -*- coding: utf8 -*-

import random
import re
import subprocess
import urllib2


def _get_packages():
    """ Lists all packaages registered on PyPI. """
    packages = list()
    response = urllib2.urlopen('https://pypi.python.org/pypi?%3Aaction=index')
    from q import q
    q(response)
    html = response.read()
    q(html)
    r = re.compile('<td><a href="/pypi/(\S+)/\S+>')
    for line in html.split('\n'):
        m = r.match(line)
        print "m is {m}".format(m=m)
        q(m)
        if m:
            q(m.group(1))
            packages.append(m.group(1))

    return packages


def wang(quiet=False):
    """ Installs a random package with `pip`. If `quiet` is true,
    PyWang won't print out the names of the packages that are
    installed. """

    packages = _get_packages()

    p = random.choice(packages)
    print "PACKAGE IS " + p

    if not quiet:
        print 'Installing {package}'.format(package=p)

    subprocess.call(['pip', 'install', p])
