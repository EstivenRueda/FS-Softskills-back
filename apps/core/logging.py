import logging


def get_finishing_school_logging(logger_name: str):
    """
    Helper method to append a 'zenapi' prefix on all of our loggers.  This enables
    us to manage them with a simple logging rule for all.
    :param logger_name: the name of the logger (usually __name__)
    :return: a logging.logger with LOGGER_PREFIX.logger
    """
    return logging.getLogger(f"finishing_school_back.{logger_name}")
