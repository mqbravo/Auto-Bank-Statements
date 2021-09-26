import tabula
import pandas as pd

dfs = tabula.read_pdf("CU_202131_CU_12011274100.pdf", pages="all")
del dfs[0]

columns = ["Date", "Ag.Movm", "Concept", "Debit", "Credit", "Balance"]
dfs = [df.dropna(axis="columns", how="all").set_axis(columns, axis=1) for df in dfs]

statement = pd.DataFrame()
for df in dfs:
    statement = statement.append(df)

statement = statement[:-2]
