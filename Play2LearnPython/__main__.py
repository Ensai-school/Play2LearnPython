# loggin and monitoring
import logging
import logging.config
import traceback
import yaml 
from queue import Queue
from time import perf_counter, sleep
# Play2LearnPython
from core.manager import Manager

def main():
    try :
        Manager().run()
    except Exception as e:
        logging.error('Ohoh ... Something unexpected happend ...')
        logging.error(e, exc_info=True)
    return

if __name__ == "__main__" :
    with open('config_logger.yml', 'r') as f:
        log_cfg = yaml.safe_load(f.read())
        logging.config.dictConfig(log_cfg)
    logging.info('Game start')
    main()
    logging.info('Game end')