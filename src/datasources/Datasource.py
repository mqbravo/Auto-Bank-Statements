from pandas import DataFrame

class Datasource:

    def extract(self)-> DataFrame:
        raise NotImplementedError()

    def upload(self) -> None:
        raise NotImplementedError()