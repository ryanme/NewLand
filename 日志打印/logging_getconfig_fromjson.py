# coding: utf8
import logging.config
import json
import os

"""
 从json获取配置
"""


def setup_logging(default_path="logging_getconfig_fromjson.json", default_level=logging.INFO, env_key="LOG_CFG"):
    path = default_path
    value = os.getenv(env_key,None)
    if value:
        path = value
    if os.path.exists(path):
        with open(path, "r") as f:
            config = json.load(f)
            logging.config.dictConfig(config)
    else:
        logging.basicConfig(level = default_level)


def func():
    logging.info("start func")
    logging.info("exec func")
    logging.info("end func")


if __name__ == "__main__":
    setup_logging(default_path="logging_getconfig_fromjson.json")
    func()
