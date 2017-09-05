"""
Install premis-tools
"""

import os
from setuptools import setup, find_packages


def scripts_list():
    """Return list of command line tools from package pas.scripts"""
    scripts = []
    for modulename in os.listdir('premis_tools/scripts'):
        if modulename == '__init__.py':
            continue
        if not modulename.endswith('.py'):
            continue
        modulename = modulename.replace('.py', '')
        scriptname = modulename.replace('_', '-')
        scripts.append('%s = premis_tools.scripts.%s:main' % (scriptname, modulename))
    print scripts
    return scripts


def main():
    """Install premis-tools"""
    setup(
        name='premis_tools',
        packages=find_packages(exclude=['tests', 'tests.*']),
        version='dev',
        entry_points={'console_scripts': scripts_list()})


if __name__ == '__main__':
    main()
