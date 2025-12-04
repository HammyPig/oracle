import os
import sys
import csv
from PyPDF2 import PdfMerger

# Get card combinations from CSV
card_combinations = {}

csv_path = "../../../../../rules/cards.csv"
with open(csv_path, "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        back = row["back"]
        if back == "-":
            back = "card-back"
        
        filename = row["filename"]
        count = int(row["count"])
        
        if back not in card_combinations:
            card_combinations[back] = {}
        
        card_combinations[back][filename] = count

# Generate PDFs
for card_back, card_fronts in card_combinations.items():
    merger = PdfMerger()

    card_back_path = f"./pdfs/{card_back}.pdf"
    merger.append(card_back_path)

    for card_front, count in card_fronts.items():
        card_front_path = f"./pdfs/{card_front}.pdf"
        for i in range(count):
            merger.append(card_front_path)

    merger.write(f"./groups/{card_back}.pdf")
    merger.close()

print("Success!")
