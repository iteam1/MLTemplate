'''
python test.py
30-Nov-2023
'''
import os
import time
from logger import setup_logger

# 1. Init
TAG = "[TEST] "

# 2. Setup logger
logger = setup_logger()
logger.info(TAG + "Setup logger")