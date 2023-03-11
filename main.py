import os

# Identify paths
SYSTEM_DRIVE = os.environ['SYSTEMDRIVE']
PC_NAME = os.environ['COMPUTERNAME']
USER_PATH = os.path.expanduser('~')
CURRENT_PATH = os.getcwd()