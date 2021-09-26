import pdfplumber as pdfp
from datetime import datetime
import pandas as pd
from numpy import nan

columns = ["Date", "Ag.Movm", "Doc/Ref", "Concept", "Amount", "Balance"]
data_clean = []

with pdfp.open("CU_202131_CU_12011274100.pdf") as file:
    for page in file.pages[1:-1]:
        content = page.extract_text()
        content_lines = content.split("\n")

        data = [i.split(" ") for i in content_lines[4:-1]]

        for i, line in enumerate(data):
            try:
                date = datetime.strptime(line.pop(0), "%d/%m/%Y").date()
                ag_movm = line.pop(0)
                doc_ref = line.pop(0)
                balance = line.pop(-1)
                amount = line.pop(-1)
                concept = nan if len(line) == 0 else " ".join(line)

                new_data_line = [date, ag_movm, doc_ref, concept, amount, balance]
                data_clean.append(new_data_line)

            except:
                print("Malformed line. Skipping 1")
                continue

df = pd.DataFrame(data_clean, columns=columns)

is_debit = [True]
current_balance = df["Balance"][0]

for balance in df["Balance"][1:]:
    is_debit.append(balance < current_balance)
    current_balance = balance

df["Is_Debit"] = is_debit

print(len(df))
