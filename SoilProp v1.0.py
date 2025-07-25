import pandas as pd
import requests
import time

# Input file
INPUT_FILE = 'Location.xlsx'

# Load coordinates
df_coords = pd.read_excel(INPUT_FILE)

# Function to fetch and structure soil data
def fetch_soil_data(lat, lon):
    url = f"https://rest.isric.org/soilgrids/v2.0/properties/query?lat={lat}&lon={lon}"
    response = requests.get(url)

    if response.status_code != 200:
        print(f"❌ Failed to fetch data for lat={lat}, lon={lon} (status {response.status_code})")
        return {}

    data = response.json()
    layers = data.get("properties", {}).get("layers", [])
    depth_dict = {}

    for layer in layers:
        prop = layer['name']
        for depth in layer['depths']:
            depth_from = depth.get('range', {}).get('from')
            depth_to = depth.get('range', {}).get('to')
            sheet_name = f"{depth_from}-{depth_to}cm"
            mean_val = depth.get('values', {}).get('mean')
            unc_val = depth.get('values', {}).get('uncertainty')

            if sheet_name not in depth_dict:
                depth_dict[sheet_name] = []

            depth_dict[sheet_name].append({
                "property": prop,
                "value_mean": mean_val,
                "value_uncertainty": unc_val
            })

    return depth_dict

# Process each point
for idx, row in df_coords.iterrows():
    lat = row['latitude']
    lon = row['longitude']
    print(f"📍 Processing point {idx + 1}/{len(df_coords)}: lat={lat}, lon={lon}")

    try:
        depth_data = fetch_soil_data(lat, lon)
        if not depth_data:
            continue

        # Output file name as "polygone_1.xlsx", "polygone_2.xlsx", ...
        file_name = f"Location_{idx + 1}.xlsx"

        # Write each depth as a sheet
        with pd.ExcelWriter(file_name) as writer:
            for depth_range, properties in depth_data.items():
                df = pd.DataFrame(properties)
                safe_sheet_name = depth_range.replace("–", "-")[:31]  # Excel max 31 chars
                df.to_excel(writer, sheet_name=safe_sheet_name, index=False)

        print(f"✅ Saved: {file_name}")

    except Exception as e:
        print(f"⚠️ Error at point {idx + 1}: {e}")

    time.sleep(1)  # Avoid API rate limit
