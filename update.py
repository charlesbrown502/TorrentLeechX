import os
import time
import requests
import logging
from logging.handlers import RotatingFileHandler

from dotenv import load_dotenv

if os.path.exists("TorrentLeech-Gdrive.txt"):
    with open("Torrentleech-Gdrive.txt", "r+") as f_d:
        f_d.truncate(0)

# the logging things
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s [%(filename)s:%(lineno)d]",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[
        RotatingFileHandler(
            "Torrentleech-Gdrive.txt", maxBytes=50000000, backupCount=10
        ),
        logging.StreamHandler(),
    ],
)

CONFIG_FILE_URL = os.environ.get('CONFIG_FILE_URL', None)
try:
    if len(CONFIG_FILE_URL) == 0:
        raise TypeError
    try:
        res = requests.get(CONFIG_FILE_URL)
        if res.status_code == 200:
            with open('config.env', 'wb+') as f:
                f.write(res.content)
                f.close()
        else:
            logging.error(f"Failed to download config.env {res.status_code}")
    except Exception as e:
        logging.error(f"CONFIG_FILE_URL: {e}")
except TypeError:
    pass

load_dotenv('config.env', override=True)
