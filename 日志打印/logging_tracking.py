# coding: utf8
import logging

"""
捕获traceback
"""

logger = logging.getLogger(__name__)
logger.setLevel(level = logging.INFO)
handler = logging.FileHandler("log.txt")
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

console = logging.StreamHandler()
console.setLevel(logging.INFO)
console.setFormatter(formatter)

logger.addHandler(handler)
logger.addHandler(console)

logger.info("Start print log")
logger.debug("Do something")
logger.warning("Something maybe fail.")
try:
    open("sklearn.txt", "rb")
except (SystemExit, KeyboardInterrupt):
    raise
except Exception:
    logger.error("Faild to open sklearn.txt from logger.error", exc_info=True)
    # logger.exception("Failed to open sklearn.txt from logger.exception")

logger.info("Finish")
