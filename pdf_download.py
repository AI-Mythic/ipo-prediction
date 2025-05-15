import requests
import os
import pandas as pd

df = pd.read_csv("datasetprospectus_pdfurl.csv")

for index, row in df.iterrows():
    filename = "_".join(row['Name'].lower().split(" ")[:2])
    
    if filename + '.pdf' not in os.listdir('prospectus'):
        try:
            url = row['PDF URL']
            if 'http' not in url:
                url = "https://www.sebi.gov.in" + url

            response = requests.get(url, timeout=60)  # <-- timeout added here
            if response.status_code == 200:
                file_path = os.path.join('prospectus', f"{filename}.pdf")
                with open(file_path, 'wb') as f:
                    f.write(response.content)
                print(f"Downloaded: {file_path}")
            else:
                print(f"Failed to download {url} - Status code: {response.status_code}")
        except Exception as e:
            print(f"Error: {row['Name']} - {e}")
