from setuptools import setup, find_packages
import sys, os

version = '0.0'

setup(name='openfsm',
      version=version,
      description="Customizations to OpenPlans for OpenFSM.net",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='openplans openfsm',
      author='Dimitris Moraitis',
      author_email='dimo@indy.gr',
      url='http://openfsm.net',
      license='GPLv2',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
