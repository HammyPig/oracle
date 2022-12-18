import os
import sys
from PyPDF2 import PdfFileMerger

oracle_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

with open(f"{oracle_dir}\cards.csv", "r") as f:
    rows = f.readlines()

header = rows.pop(0)

for i in range(len(rows)):
    rows[i] = rows[i].rstrip("\n")
    rows[i] = rows[i].split(",")

merger = PdfFileMerger()

# For every card, add card and corresponding back x amount of times to pdf
for row in rows:
    name = row[0]
    count = int(row[1])
    front = row[2]
    back = row[3]
    card_type = row[4]

    if card_type == "back":
        continue

    if back == "-":
        back = "card-back"

    front_pdf_path = f"_pdfs/{front}.pdf"
    back_pdf_path = f"_pdfs/{back}.pdf"

    for i in range(count):
        merger.append(front_pdf_path)
        merger.append(back_pdf_path)

merger.write("front-backs.pdf")
merger.close()

print("Success!")
