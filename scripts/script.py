from pathlib import Path
import json

# Define the folder path
folder = Path("../regionData")

# Get all JSON files
json_files = folder.glob("*.json")

# Loop through and modify each file
for file in json_files:
    with open(file, "r", encoding="utf-8") as f:
        data = json.load(f)
    print 
    for indicator in data["indicators"]:
        for val in indicator['yearlyData']:
            val['year'] = int(val['year'])
            try:
                val['value'] = float(val['value'])
                if val['value'].is_integer():
                    val['value'] = int(val['value'])
            except ValueError:
                print(val['value'])            
    with open(file, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)