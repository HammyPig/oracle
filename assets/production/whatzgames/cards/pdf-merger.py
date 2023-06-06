import os
import sys
from PyPDF2 import PdfMerger


card_combinations = {
    "card-back": {
        "attack": 15,
        "backstab": 2,
        "capture": 3,
        "destroy": 3,
        "heist": 1,
        "sabotage": 1,
        "spy": 1,
        "defend": 9,
        "goody-bag": 2,
        "goody-bag-plus": 1,
        "barracks": 4,
        "farm": 3,
        "fort": 2,
        "spell-tower": 3,
        "barrier": 1,
        "black-hole": 1,
        "blood-magic": 1,
        "nullify": 1
    },

    "card-back-role": {
        "cultist": 1,
        "demon-lord": 1,
        "knight": 1,
        "the-crown": 1,
        "usurper": 1
    },

    "card-back-health-bar": {
        "health-bar": 5
    },

    "card-back-oracle": {
        "oracle": 1
    }
}

fronts = PdfMerger()
backs = PdfMerger()

for card_back, card_fronts in card_combinations.items():
    card_back_path = f"./pdfs/{card_back}.pdf"

    for card_front, count in card_fronts.items():
        card_front_path = f"./pdfs/{card_front}.pdf"
        for i in range(count):
            fronts.append(card_front_path)
            backs.append(card_back_path)

fronts.write(f"./fronts.pdf")
fronts.close()

backs.write(f"./backs.pdf")
backs.close()

print("Success!")
