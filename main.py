import os
import pathlib
import datetime
import logging


# use custom logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
filehandler = logging.FileHandler(pathlib.Path("logs", "file_delete_record.log"))    # location for log file
logger.addHandler(filehandler)
formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(message)s : %(name)s")   # log message format
filehandler.setFormatter(formatter)

# initialize dir location where files will be deleted at
search_loc = pathlib.Path("/", "Users", "architkumar", "Downloads")

# get all files that match your pattern
matches = [i for i in search_loc.glob("*.zip")]     # describe desired pattern here (UNIX style pattern matching)
matches_creation_dts = [datetime.date.fromtimestamp(pathlib.Path(m).stat().st_mtime) for m in matches]
matched_dict = dict(zip(matches, matches_creation_dts))

today = datetime.date.today()
logger.info("Start Run...")
counter = 0     # variable that records number of files deleted
for k, v in matched_dict.items():
    # delete the matched file if it is at least a day older
    if v < today:
        counter += 1
        logger.debug(f"Deleting {k}")
        os.remove(k)
    else:
        pass

# log delete status
if counter == 0:
    logger.info("No files deleted.")
else:
    logger.info(f"Total num of files deleted = {counter}")

