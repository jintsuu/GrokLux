import os
from os import getenv

from logger import SingletonLogger

from dotenv import load_dotenv

logger = SingletonLogger().get_logger()
load_dotenv()

from Bot.app import App

if __name__ == '__main__':
    logger.info("Starting app.")
    app = App()
    app.run(token=getenv("TOKEN"))