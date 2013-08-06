#!/usr/bin/env python

#-----------------------------------------------------------------------------
# Copyright (c) 2013, The BiPy Development Team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file COPYING.txt, distributed with this software.
#-----------------------------------------------------------------------------

from pyqi.core.interfaces.optparse import (OptparseOption,
                                           OptparseUsageExample,
                                           OptparseResult)
from pyqi.core.interfaces.optparse.output_handler import write_string
from pyqi.commands.make_bash_completion import CommandConstructor

__author__ = "Daniel McDonald"
__copyright__ = "Copyright 2013, The QCLI Project"
__credits__ = ["Daniel McDonald", "Jai Ram Rideout", "Doug Wendel", "Greg Caporaso"]
__license__ = "BSD"
__version__ = "0.1.0-dev"
__maintainer__ = "Daniel McDonald"
__email__ = "mcdonadt@colorado.edu"

# How you can use the command from the command line
### need to make sure comments desc usage_examples goes into make_cli template (make_optparse?)
usage_examples = [
    OptparseUsageExample(ShortDesc="Create a bash completion script",
                         LongDesc="Create a bash completion script for use with a QCLI driver",
                         Ex="%prog --command-config-module pyqi.interfaces.optparse.config --driver-name pyqi -o ~/.bash_completion.d/pyqi")
]

### need to make sure comments desc input goes into make_cli template (make_optparse?)
inputs = [
    OptparseOption(InputType=str,
                   Parameter=CommandConstructor.Parameters['command_config_module'],
                   # Required=True implied by Parameter
                   # Name='command_cfg_directory', implied by Parameter
                   ShortName=None,
                   # Help is pulled from parameter since Parameter is not None
                   InputHandler=None), # optparse handles str just fine
    OptparseOption(InputType=str,
                   Parameter=CommandConstructor.Parameters['driver_name'],
                   # Required=True implied by Parameter
                   # Name='driver_name', implied by Parameter
                   ShortName=None,
                   # Help is pulled from parameter since Paramter is not None
                   InputHandler=None),
    OptparseOption(InputType='new_filepath',
                   Parameter=None, #
                   Required=True,
                   Name='output_fp',
                   ShortName='o',
                   Help="Output file path",
                   InputHandler=None)
    ]

### need to make sure comments desc output goes into make_cli template (make_optparse?)
outputs = [
    OptparseResult(OutputType=None, ### do we need an outputtype?
                   Parameter=None,
                   Name='output_fp', # if specified, must exist as an input
                   OutputHandler=write_string,
                   ResultKey='result')
    ]