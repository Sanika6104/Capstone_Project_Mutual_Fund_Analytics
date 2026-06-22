import requests
import pandas as pd
import os

codes = [
    125497,
    119551,
    120503,
    118632,
    119092,
    120841
]

output_folder = "data/raw"

for code in codes:
    url = f"https://api.mfapi.in/mf/{code}"

    try:
        response = requests.get(url)

        data = response.json()

        nav_df = pd.DataFrame(data["data"])

        filename = f"nav_{code}.csv"

        nav_df.to_csv(
            os.path.join(output_folder, filename),
            index=False
        )

        print(f"Saved {filename}")

    except Exception as e:
        print(f"Error fetching {code}: {e}")