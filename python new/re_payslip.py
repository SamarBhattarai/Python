import os
import re
from pathlib import Path

string = os.getcwd()
print(string)
path = Path(r"D:\Python\Python\python new")
folder_path = path / "Pay_Slip_Samip"

for file_path in folder_path.glob("*pdf"):
    filename = file_path.name

    # Regex to capture: Name_DDMMYYYY.pdf
    match = re.search(r'(.+)_(\d{2})(\d{2})(\d{4})\.pdf', filename)

    if match:
        name_part, day, month, year = match.groups()
        
        # 3. Create the new sortable name: YYYY-MM-DD_Name.pdf
        new_name = f"{year}-{month}-{day}_{name_part}.pdf"
        # Rename the file
        file_path.rename(folder_path / new_name)
        print(f"Successfully Renamed: {filename} -> {new_name}")