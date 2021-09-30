import tabula
import pandas as pd
from datasources import Datasource


class ScotiabankScrapper(Datasource):
    def __init__(self, filepath) -> None:
        self.filepath = filepath

    def extract(self) -> pd.DataFrame:

        dfs = tabula.read_pdf(self.filepath, pages="all")
        del dfs[0]

        columns = ["Date", "Ag.Movm", "Concept", "Debit", "Credit", "Balance"]
        dfs = [
            df.dropna(axis="columns", how="all").set_axis(columns, axis=1) for df in dfs
        ]

        statement = pd.DataFrame()
        for df in dfs:
            statement = statement.append(df)

        statement = statement[:-2]

        statement = statement[~statement["Date"].isna()]
        remove_comma_and_to_num(statement, ["Debit", "Credit", "Balance"])

        return statement

    def upload(self) -> None:
        return super().upload()


def remove_comma_and_to_num(df, columns):
    df[columns] = df[columns].apply(lambda df: df.str.replace(",", ""))
    df[columns] = df[columns].apply(pd.to_numeric)
