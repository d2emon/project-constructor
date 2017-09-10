#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import argparse

from utils import query_yes_no
from template import FlaskProjectTemplate, FlaskDbProjectTemplate, generate_brief, generate_errorlist
from project import FlaskProject


def generate_crsf_secret_key():
    return


def main(argv):
    parser = argparse.ArgumentParser(description='Create a skeleton application using some command line options.')
    parser.add_argument('appname', help='The application name')
    parser.add_argument('-b', '--bower', help='Dependencies installed using bower')
    parser.add_argument('-n', '--no-debug', action='store_false')
    parser.add_argument('-v', '--virtualenv', action='store_true')
    parser.add_argument('-d', '--database', action='store_true')
    parser.add_argument('-g', '--git', action='store_true')
    args = parser.parse_args()

    bower = None
    if args.bower:
        bower = args.bower.split(',')
    virtualenv = args.virtualenv
    debug = args.no_debug
    appname = args.appname
    database = args.database
    git = args.git

    if database:
        project_template = FlaskDbProjectTemplate()
    else:
        project_template = FlaskProjectTemplate()
    project = FlaskProject(appname, project_template)

    project.debug = debug

    project.bower = bower
    project.virtualenv = virtualenv
    project.git = git

    print(generate_brief(project.brief_var))
    if project_template.externals.has_errors:
        errors = project_template.externals.errors
        print(generate_errorlist({'errors': errors, }))
        sys.exit(1)

    if query_yes_no("Is this correct ?"):
        project.install()
    else:
        print("Aborting")
        sys.exit(0)


if __name__ == '__main__':
    main(sys.argv)
