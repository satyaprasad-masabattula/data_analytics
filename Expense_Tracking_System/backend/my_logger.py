import logging


def set_my_looger(name,fileName='server.log',level=logging.DEBUG):
    log = logging.getLogger(name)
    log.setLevel(level)
    file_hnadler = logging.FileHandler(fileName)
    format_str = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_hnadler.setFormatter(format_str)
    log.addHandler(file_hnadler)
    return log