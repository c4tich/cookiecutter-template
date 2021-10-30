Developers Guide
################

.. include:: ../../../CONTRIBUTING.rst


.. _testing-label:

Testing
=======

The {{cookiecutter.package_display_name}} project implements a regression
test suite that improves developer productivity by identifying capability
regressions early.

Developers implementing fixes or enhancements must ensure that they have
not broken existing functionality. The {{cookiecutter.package_display_name}}
project provides some convenience tools so this testing step can be quickly
performed.

Use the Makefile convenience rules to run the tests.

.. code-block:: console

    ({{cookiecutter.package_name}}) $ pytest

To run tests verbosely use:

.. code-block:: console

    ({{cookiecutter.package_name}}) $ pytest -vvv

Release Process
===============

# TODO