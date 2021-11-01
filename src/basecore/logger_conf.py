import logging


logger_format = '%(asctime)s - [%(levelname)s] - %(name)s - (%(filename)s).%(funcName)s(%(lineno)d) - %(message)s'


#  logger_handlers
def get_file_handler():
    #  writes to the log if warning level
    file_handler = logging.FileHandler('logfile.log')
    file_handler.setLevel(logging.WARNING)
    file_handler.setFormatter(logging.Formatter(logger_format))
    return file_handler


def get_stream_handler():
    #  writes to the console all
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.INFO)
    stream_handler.setFormatter(logging.Formatter(logger_format))
    return stream_handler


def get_logger(name):
    #  create logger. Add name=__name__!!
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    logger.addHandler(get_file_handler())
    logger.addHandler(get_stream_handler())
    return logger
