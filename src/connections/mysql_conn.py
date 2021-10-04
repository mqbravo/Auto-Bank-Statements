from sqlalchemy import create_engine
from config.config_reader import read_yaml
from string import Template
from util.singleton_meta import SingletonMeta
from log.logger import logger


class MySQLConnection(metaclass=SingletonMeta):
    def __init__(self) -> None:
        mysql_config = read_yaml("connections")["mysql"]

        conn_params = {
            "user": mysql_config["user"],
            "password": mysql_config["password"],
            "host": mysql_config["host"],
            "port": mysql_config["port"],
        }

        logger.info(
            f"Creating MySQL engine with parameters user={conn_params['user']}, host={conn_params['host']}, port={conn_params['port']}..."
        )

        conn_string = Template(mysql_config["conn_string_template"]).substitute(
            **conn_params
        )

        try:
            self.engine = create_engine(conn_string)
            logger.info("Engine created successfully!")
        except:
            logger.exception("Error creating MySQL engine")
