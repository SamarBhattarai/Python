import os
from pathlib import Path
from pypdf import PdfWriter

# 1. Setup paths
base_path = Path(__file__).parent
folder_path = base_path / "Pay_Slip_Samip"
output_filename = "Merged_Pay_Slips_2023-2026.pdf"

# 2. Get and sort all PDF files
# Because you renamed them YYYY-MM-DD, sorting them alphabetically
# naturally puts them in chronological order.
pdf_files = sorted(list(folder_path.glob("*.pdf")))

if not pdf_files:
    print("No PDF files found to merge!")
else:
    merger = PdfWriter()

    print(f"Merging {len(pdf_files)} files...")

    for pdf in pdf_files:
        print(f"Adding: {pdf.name}")
        merger.append(pdf)

    # 3. Save the final merged document
    merger.write(base_path / output_filename)
    merger.close()

    print(f"\nSuccess! All files merged into: {output_filename}")