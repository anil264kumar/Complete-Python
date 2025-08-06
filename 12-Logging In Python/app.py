import logging

## logging setting

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.FileHandler("app1.log"),
        logging.StreamHandler()
    ]
)



## create logger
logger = logging.getLogger("ArithematicApp")

def add(a,b):
    result = a+b
    logger.debug(f"Adding {a}+{b} = {result}")
    return result

def subtract(a,b):
    result = a-b
    logger.debug(f"Subtracting {a}-{b} = {result}")
    return result

def multiply(a,b):
    result = a*b
    logger.debug(f"Multiplying {a}+{b} = {result}")
    return result

def divide(a,b):
    try:
        result=a/b
        logger.debug(f"Dividing {a}/{b} = {result}")
        return result
    except ZeroDivisionError :
        logger.error("Division by zero error")
        return None
    

add(12,45)
subtract(34,24)
multiply(12,13)
divide(56,0)
