import zipfile
from pathlib import Path

src_docx = Path(r"z:\SKRIPSII\SKRIPSI-arthur\scratch\original_binary.docx")
dst_docx = Path(r"z:\SKRIPSII\SKRIPSI-arthur\01_Naskah_Utama\Proposal_Arthur_PokemonTCG.docx")

old_dosbim = "Dr. Diana Frederica, S.E., M.Ak., CFP®., CHCP-A"
new_dosbim = "Dr. Fredella Colline, S.E., M.M., CFP®, PFM, CHCP-A"

old_dekan = ", selaku Dekan Fakultas Ekonomi dan Bisnis UKRIDA sekaligus Dosen Pembimbing Skripsi,"
new_dekan = ", selaku Dosen Pembimbing Skripsi,"

old_nidn = "0315088201"
new_nidn = "[NIDN_DOSEN]"

with zipfile.ZipFile(src_docx, 'r') as zin:
    with zipfile.ZipFile(dst_docx, 'w') as zout:
        for item in zin.infolist():
            buffer = zin.read(item.filename)
            if item.filename == 'word/document.xml':
                xml_text = buffer.decode('utf-8')
                
                # Check replacements
                assert old_dosbim in xml_text, f"Target '{old_dosbim}' not found in document.xml!"
                assert old_dekan in xml_text, f"Target '{old_dekan}' not found in document.xml!"
                assert old_nidn in xml_text, f"Target '{old_nidn}' not found in document.xml!"
                
                xml_text = xml_text.replace(old_dosbim, new_dosbim)
                xml_text = xml_text.replace(old_dekan, new_dekan)
                xml_text = xml_text.replace(old_nidn, new_nidn)
                
                buffer = xml_text.encode('utf-8')
                zout.writestr(item, buffer)
            else:
                # Copy as-is with original compression type and metadata
                zout.writestr(item, buffer)

print("Surgical zip packaging complete!")
