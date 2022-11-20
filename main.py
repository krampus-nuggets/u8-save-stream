# Package Imports
import os
import sys

# Internal Imports
from modules.engine import download_all_streams
from modules.utils import check_config, read_config, term_output, is_windows, get_filenames, get_valid_streams


root_dir = os.path.dirname(__file__)
config_uri = f"{root_dir}\\config.yaml" if is_windows() else f"{root_dir}/config.yaml"
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

# Get saved stream names
filenames = get_filenames(root_dir, "mp4")

# Get streams that were missed
unsaved_streams = get_valid_streams(filenames, streams)

# CHECK - Valid list returned containing stream dictionaries
if (unsaved_streams == None):
  term_output("error", "Failed to retrieve valid streams")
  sys.exit(1)

# Download Streams in config file
try:
  download_all_streams(streams)
except KeyboardInterrupt:
  term_output("info", "Process Exited!")
  sys.exit(0)
