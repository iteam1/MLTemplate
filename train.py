'''
python train.py
30-Nov-23
'''
import os
import time
import argparse
from logger import setup_logger

# 1. Parse arguments

# 2. Init
TAG = "[TRAIN] "

# 3. Setup logger
logger = setup_logger()
logger.info(TAG + "Setup logger")