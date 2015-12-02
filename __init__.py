"""
EM
==

Collects
  1. A transfer matrix or transmission line routine for multilayer
  reflection, transmission and absorption.
  2. A 2D plane-wave expansion routine.
  3. Small tools for parametric sweep generation.

"""
import sys
import numpy as np
from . import pwe
from . import multi
from . import tools
