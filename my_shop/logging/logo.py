import logging

logging.basicConfig(format='%(asctime)s: %(level)s: %(message)%s',
                    filename='example.log',
                    level=logging.warning)

logging.debug("Отладочная информация")
logging.info("Сообщение")
logging.warning("Предупреждение")
logging.error("Серьезная Ошибка")
logging.critical("Критическая ошибка")
