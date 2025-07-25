# Soil Property Downloader – Location-Based Version

This Python script allows you to automatically download soil property data from the [SoilGrids API by ISRIC](https://soilgrids.org/) for multiple geographic locations. Each location's data is saved to a separate Excel file, with each soil depth as a separate worksheet.

---

## 📥 Input File

The script reads coordinates from an Excel file named `Location.xlsx` with the following format:

| latitude | longitude |
|----------|-----------|
| 36.85    | 10.33     |
| 35.71    | 9.55      |

---

## 📦 Requirements

- Python 3.x
- Required libraries:
  ```bash
  pip install pandas openpyxl requests
  ```

---

## 🚀 How to Use

1. Place `Location.xlsx` in the same folder as the script.
2. Run the script using Spyder or any Python environment.
3. For each location:
   - The script queries the SoilGrids REST API.
   - Downloads all available soil properties.
   - Organizes data by depth range (0–5cm, 5–15cm, etc.).
   - Saves the results in `location_1.xlsx`, `location_2.xlsx`, etc.
   - Each depth range is stored in a separate worksheet.

---

## 🧾 Output Example

Each output Excel file will have:

### Sheets:

| Sheet Name | Contents                     |
|------------|------------------------------|
| 0-5cm      | sand, clay, silt, pH, etc.   |
| 5-15cm     | sand, clay, silt, pH, etc.   |

### Each Sheet Contains:

| property | value_mean | value_uncertainty |
|----------|------------|-------------------|
| sand     | 23.5       | 1.2               |
| clay     | 12.3       | 0.8               |

---

## ⚠️ Notes

- If the API fails for a point, it will skip and log the error.
- A 1-second delay between requests prevents hitting API rate limits.
- Sheet names are trimmed to 31 characters (Excel limitation).

---

## 📚 License and Citation

This script uses data from ISRIC SoilGrids. Please cite accordingly when using this tool in research.

🔗 https://soilgrids.org/


[![DOI](https://zenodo.org/badge/1026375010.svg)](https://doi.org/10.5281/zenodo.16423400)


