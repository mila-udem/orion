#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
:mod:`orion.core.cli.db_main` -- Module containing database related operations
==============================================================================

.. module:: db_main
   :platform: Unix
   :synopsis: Root command for database operations

"""
import logging

from orion.core.utils import module_import

log = logging.getLogger(__name__)


def add_subparser(parser):
    """Add the subparsers that needs to be used for this command"""
    # Fetch experiment name, user's script path and command line arguments
    # Use `-h` option to show help

    db_parser = parser.add_parser('db', help='test_db help')
    subparsers = db_parser.add_subparsers(help='sub-command help')

    load_modules_parser(subparsers)

    return db_parser


def load_modules_parser(subparsers):
    """Search through the `cli.db` folder for any module containing a `get_parser` function"""
    modules = module_import.load_modules_in_path('orion.core.cli.db',
                                                 lambda m: hasattr(m, 'add_subparser'))

    for module in modules:
        get_parser = getattr(module, 'add_subparser')
        get_parser(subparsers)
