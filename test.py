'''
python test.py
30-Nov-2023
'''
import os
import time
import argparse
from logger import setup_logger

# 1. Parse arguments

# 2. Init
TAG = "[TEST] "

# 3. Setup logger
logger = setup_logger()
logger.info(TAG + "Setup logger")