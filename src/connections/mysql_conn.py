from sqlalchemy import create_engine
from config.config_reader import read_yaml
from string import Template


class MySQLConnection:
    def __init__(self) -> None:
        pass

    def get_engine(self):
        mysql_config = read_yaml("connections")["mysql"]

        conn_params = {
            "user": mysql_config["user"],
            "password": mysql_config["password"],
            "host": mysql_config["host"],
            "port": mysql_config["port"],
        }

        conn_string = Template(mysql_config["conn_string_template"]).substitute(
            **conn_params
        )

        print(conn_string)

        return create_engine(conn_string)
