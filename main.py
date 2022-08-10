import os
import pathlib
import datetime
import logging


# use custom logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
filehandler = logging.FileHandler("logs/file_delete_record.log")
logger.addHandler(filehandler)
formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(message)s : %(name)s")
filehandler.setFormatter(formatter)


search_loc = pathlib.Path("/", "Users", "architkumar", "Downloads")
matches = [i for i in search_loc.glob("*.zip")]
matches_creation_dts = [datetime.date.fromtimestamp(pathlib.Path(m).stat().st_mtime) for m in matches]
matched_dict = dict(zip(matches, matches_creation_dts))
today = datetime.date.today()
logger.info("Start Run...")
counter = 0
for k, v in matched_dict.items():
    if v < today:
        counter += 1
        logger.debug(f"Deleting {k}")
        os.remove(k)
    else:
        pass

if counter == 0:
    logger.info("No files deleted.")
else:
    logger.info(f"Total num of files deleted = {counter}")

