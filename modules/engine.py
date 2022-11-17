# Package Imports
import ffmpeg
import concurrent.futures as futures

# Internal Imports
from modules.utils import term_output

# Download Stream | Input: Stream_Object
def download_stream(payload):
  try:
    # Input Stream
    input_file = payload["streamFile"]
    stream = ffmpeg.input(
      input_file,
      thread_queue_size="8192",
      protocol_whitelist="file,http,https,tcp,tls,crypto"
    )

    # Overwrite Output File
    # stream = ffmpeg.overwrite_output(stream)

    # Construct Output File
    file_name = payload["filename"]
    file_ext = payload["extension"]
    output_file = f"{file_name}.{file_ext}"

    # Output Stream
    stream = ffmpeg.output(
      stream,
      output_file,
      acodec="copy",
      vcodec="copy"
    )

    # Output Stream Overwrite
    stream = ffmpeg.overwrite_output(stream)

    # Invoke FFMPEG
    ffmpeg.run(stream)

    return True
  except Exception as error:
    term_output("error", error)
    return False

# Download All Streams | Input: Array[Stream_Objects]
def download_all_streams(payload):
  try:
    with futures.ThreadPoolExecutor(max_workers=5) as executor:
      executor.map(download_stream, payload)
      executor.shutdown(wait=True)
    
    return True
  except Exception:
    return False
