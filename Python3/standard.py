""" This file presents an example of how to follow pep8 coding standards and
more importantly, how not to. Notice how the line length is limited to 
a fixed amount of characters. This will allow me to open two files next
to eachother comfortably.

# Include Meta Data when appropriate at the top of the file 

"""

__version__ = '0.1'
__author__ = 'Ben Larking'

# imports should be at the top of the file and should ordered as such
import os
import sys
from subprocess import Popen, PIPE

import pandas as pd 
from pyspark import spark

from mypkg import Aclass
from mypkg2import Bclass

# vs ...

import os
from mypkg2import Bclass
import pandas as pd 
from pyspark import spark
from mypkg import Aclass
from subprocess import Popen, PIPE
import sys


class ExampleClass:
    """
    This is a class representing the Batch State Object, 2 white space from imports
    """


# White Space can make a huge difference. 
# Correct 

# Aligned with opening delimiter.
foo = long_function_name(var_one, var_two,
                         var_three, var_four)

# Incorrect 
# Arguments on first line forbidden when not using vertical alignment.
foo = long_function_name(var_one, var_two,
    var_three, var_four)

# Add 4 spaces (an extra level of indentation) to distinguish arguments
# from the rest.
def long_function_name(
        var_one, var_two, var_three,
        var_four):
		""" this is the long function name, it does x """
    print(var_one)


# Further indentation required as indentation is not distinguishable.
def long_function_name(
    var_one, var_two, var_three,
    var_four):
    print(var_one)


# Correct:
# easy to match operators with operands
income = (gross_wages
          + taxable_interest
          + (dividends - qualified_dividends)
          - ira_deduction
          - student_loan_interest)

# Wrong:
# operators sit far away from their operands
income = (gross_wages +
          taxable_interest +
          (dividends - qualified_dividends) -
          ira_deduction -
          student_loan_interest)


# Please be a little more descriptive 
for x in y:
	do abc 

# What are we trying to catch here? 
try:
	thing_that_might_fail
except Exception 

try: 
	thing_that_might_fail
except ValueError:
	handle_value_error
except TypeError:
	handle_type_error
