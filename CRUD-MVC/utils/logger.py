import logging

logging.basicConfig(level=logging.INFO, filename = 'a',format'%(asctime)s - %(levelname)s - %(message)s') #log file name

def lo_info(mensaje):
    logging.info(mensaje)
    
def log_error(mensaje):
    logging.error(mensaje)