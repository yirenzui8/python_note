#!/usr/bin/env python3.5
import sys
import readline
import rlcompleter
import os
readline.parse_and_bind('tab: complete')
histfile = os.path.join(os.environ['HOME'],'.pythonhistory')

