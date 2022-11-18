# Package Imports
import os
import sys

# Internal Imports
from modules.engine import download_all_streams

root_dir = os.path.dirname(__file__)
config_uri = f"{root_dir}\\config.yaml"
config_exists = check_config(config_uri)

# CHECK - Config URI is valid
if (not config_exists):
  term_output("error", "Config file not found, please define config.yaml in root")
  sys.exit(1)

config_data = read_config(config_uri)

# CHECK - YAML data in config file is valid
if (config_data == None):
  term_output("error", "Config file not found, please define config.yaml in root")
  sys.exit(1)

# Get stream data in config
streams = config_data["streams"]

# Download Streams in config file
try:
  download_all_streams(streams)
except KeyboardInterrupt:
  term_output("info", "Process Exited!")
  sys.exit(0)
