from setuptools import setup, find_packages
import sys, os

version = '0.0'

setup(name='openfsm',
      version=version,
      description="Customizations to OpenPlans for OpenFSM.net",
      long_description="""\
""",
      # Get more strings from https://pypi.org/pypi?:action=list_classifiers
      classifiers=[
          "Development Status :: 3 - Alpha",
          "Environment :: Plugins",
          "Environment :: Web Environment",
          "Framework :: Plone",
          "Framework :: Zope2",
          "Framework :: Zope3",
          "Intended Audience :: End Users/Desktop",
          "Intended Audience :: System Administrators",
          "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
          "Operating System :: OS Independent",
          "Programming Language :: JavaScript",
          "Programming Language :: Python",
          "Programming Language :: Python :: 2.6",
          "Programming Language :: Python :: 2.7",
          "Topic :: Office/Business :: Office Suites",
          "Topic :: Software Development :: Libraries :: Python Modules",
      ],
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
          'Products.LinguaPlone==2.1.1',
          'plone.browserlayer==1.0.1',
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
