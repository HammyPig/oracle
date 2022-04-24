import pandas as pd

df = pd.read_csv("source.csv")
df.dropna(subset=["provider"], inplace=True)
df.fillna("", inplace=True)
df.sort_values(by=["card"], inplace=True)

html = """<table class=\"attribution\">
    <tr>
        <th style=\"text-align:left\">Card</th>
        <th style=\"text-align:right\">Attribution</th>
    </tr>
"""

for row in df.itertuples():
    card_name = row[2]
    provider = row[3]
    source_link = row[4]
    attribution_link = row[5]

    if not attribution_link:
        raise ValueError("Attribution link not found")

    filename = card_name.lower()
    filename = filename.replace(" ", "-")
    filename = filename.replace("+", "-plus")

    html += f"""    <tr>
        <td><a href=\"https://oraclecardgame.com/wp-content/uploads/{filename}.jpg\">{card_name}</a></td>
        <td style=\"text-align:right\"><a href=\"{attribution_link}\">Vector created by {provider}</a></td>
    </tr>
"""

html += "</table>"

with open("attributions.html", "w") as f:
    f.write(html)
