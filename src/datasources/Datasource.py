from typing import Optional
from pandas import DataFrame


class Datasource:
    def __init__(self) -> None:
        self.data: Optional[DataFrame] = None

    def extract(self) -> DataFrame:
        raise NotImplementedError()

    def upload(self) -> None:
        raise NotImplementedError()
