import logging

def setup_logger(name,log_file='server.log',level=logging.DEBUG):
    logger=logging.getLogger(name)
    logger.setLevel(level)
    file_handler = logging.FileHandler(log_file)
    formatter = logging.Formatter('%(asctime)s- %(name)s- %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger
# import logging
# import sys
#
# def setup_logger(name, log_file='server.log', level=logging.DEBUG):
#     # Create a logger object
#     logger = logging.getLogger(name)
#     logger.setLevel(level)
#
#     # Avoid adding duplicate handlers if the logger already exists
#     if not logger.handlers:
#         # File handler for logging into a file
#         file_handler = logging.FileHandler(log_file)
#         file_handler.setLevel(level)
#
#         # Console handler for logging to the console (stdout)
#         console_handler = logging.StreamHandler()
#         console_handler.setLevel(level)
#
#         # Define log format
#         formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
#         file_handler.setFormatter(formatter)
#         console_handler.setFormatter(formatter)
#
#         # Add handlers to the logger
#         logger.addHandler(file_handler)
#         logger.addHandler(console_handler)
#     sys.stdout.flush()
#
#     return logger
# import logging
#
# def setup_logger(name, log_file='server.log', level=logging.DEBUG):
#     logger = logging.getLogger(name)
#     logger.setLevel(level)
#     file_handler = logging.FileHandler(log_file)
#     formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
#     file_handler.setFormatter(formatter)
#     logger.addHandler(file_handler)
#     return logger
#
# logger = setup_logger('test_logger')
#
# # Test logging
# logger.info('This is an info log')
# logger.error('This is an error log')
