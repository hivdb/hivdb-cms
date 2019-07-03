#! /usr/bin/env python

import os
import re
import json
import yaml
from yaml import Loader
from distutils.dir_util import copy_tree

BASEDIR = os.path.dirname(os.path.abspath(__file__))
PAGEDIR = os.path.join(BASEDIR, 'pages')
IMAGEDIR = os.path.join(BASEDIR, 'images')
BUILDDIR = os.path.join(BASEDIR, 'build')

YAML_PATTERN = re.compile(r'^(.*)\.ya?ml$')


def main():
    os.makedirs(BUILDDIR, exist_ok=True)
    for folder, _, files in os.walk(PAGEDIR):
        for filename in files:
            if not YAML_PATTERN.match(filename):
                continue
            yamlpath = os.path.join(folder, filename)
            rel_yamlpath = os.path.relpath(yamlpath, BASEDIR)
            jsonpath = os.path.join(
                BUILDDIR, YAML_PATTERN.sub(r'\1.json', rel_yamlpath))
            os.makedirs(os.path.dirname(jsonpath), exist_ok=True)
            with open(yamlpath) as yamlfp, open(jsonpath, 'w') as jsonfp:
                data = yaml.load(yamlfp, Loader=Loader)
                json.dump(data, jsonfp)
                print('create: {}'.format(jsonpath))
    copy_tree(IMAGEDIR, os.path.join(BUILDDIR, 'images'))


if __name__ == '__main__':
    main()
