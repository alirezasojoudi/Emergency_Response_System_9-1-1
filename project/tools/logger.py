import logging

class Logger:
    logging.basicConfig(
        format='%(asctime)s - %(levelname)s - %(message)s',
        filename=r"D:\python 3710\project\file_work\emergency.log",
        level=logging.INFO,
        encoding="utf-8"
    )

    def info(self, message):
        logging.info(message)

    def error(self, message):
        logging.error(message)