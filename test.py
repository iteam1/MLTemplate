'''
python test.py
30-Nov-23
'''
import os
import time
import argparse
from logger import setup_logger

# 1. Parse arguments

# 2. Init
TAG = "[TEST] "
DELAY_TIME = 2

# 3. Setup logger
logger = setup_logger()
logger.info(TAG + "Setup logger")

# 4. Run
logger.info(TAG + "Start testing")
time.sleep(DELAY_TIME)
logger.info(TAG + "End testing")

# 5. Update status for MLAPI