"""
Layer 3 Execution Script: Verify PDF File Integrity and Extract Page Counts
Checks binary magic header %PDF- and extracts basic metrics using PyMuPDF.
"""

import os
import sys

def verify_pdfs(base_dir):
    print(f"Scanning directory: {base_dir}")
    valid_count = 0
    invalid_count = 0

    try:
        import fitz  # PyMuPDF
        has_fitz = True
    except ImportError:
        has_fitz = False

    for root, _, files in os.walk(base_dir):
        for f in files:
            if f.lower().endswith(".pdf"):
                full_path = os.path.join(root, f)
                size = os.path.getsize(full_path)
                
                # Check binary header
                with open(full_path, "rb") as fp:
                    header = fp.read(5)

                if header.startswith(b"%PDF"):
                    pages = "N/A"
                    if has_fitz:
                        try:
                            doc = fitz.open(full_path)
                            pages = len(doc)
                            doc.close()
                        except Exception as e:
                            pages = f"Error: {e}"
                    print(f"[OK] {f} | Size: {size:,} bytes | Pages: {pages}")
                    valid_count += 1
                else:
                    print(f"[INVALID/CORRUPT] {f} | Header: {header} | Size: {size} bytes")
                    invalid_count += 1

    print("\n" + "="*50)
    print(f"Summary: {valid_count} Valid PDFs, {invalid_count} Invalid Files")
    print("="*50)
    return invalid_count == 0

if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else "05_Referensi_Jurnal_PDF"
    success = verify_pdfs(target)
    sys.exit(0 if success else 1)
