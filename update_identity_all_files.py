"""
Script to update Author Name (Arthur Reezan) and NIM (312023002) across all files in the repository.
"""
import os
import re

TARGET_NAME = "Arthur Reezan"
TARGET_NIM = "312023002"

OLD_NIMS = ["312023002", "312023002", "312023002"]
OLD_NAMES = ["Arthur Reezan", "Arthur Reezan"]

def update_file(filepath):
    if not os.path.exists(filepath):
        return
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"Skipping {filepath}: {e}")
        return

    original = content
    # Replace NIMs
    for old_nim in OLD_NIMS:
        content = content.replace(old_nim, TARGET_NIM)
    # Replace Names
    for old_name in OLD_NAMES:
        content = content.replace(old_name, TARGET_NAME)

    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated: {filepath}")

def main():
    repo_root = r"z:\Skripsi"
    
    # Specific key files
    key_files = [
        os.path.join(repo_root, r"latex\Skripsi_Arthur.tex"),
        os.path.join(repo_root, r"latex\patch_skripsi.py"),
        os.path.join(repo_root, r"01_Naskah_Utama\sync_markdown_from_tex.py"),
        os.path.join(repo_root, r"01_Naskah_Utama\SKRIPSI_ARTHUR_LENGKAP_PRISM.md"),
        os.path.join(repo_root, r"03_Draft_Per_Bab\SKRIPSI_LENGKAP_BAB_1_SAMPAI_5.md"),
        os.path.join(repo_root, r"03_Draft_Per_Bab\PROPOSAL_SKRIPSI_LENGKAP.md"),
        os.path.join(repo_root, r"README.md"),
    ]
    
    for kf in key_files:
        update_file(kf)

    # Walk directory to catch any other markdown, latex, html, txt, or python files
    for root, dirs, files in os.walk(repo_root):
        if ".git" in root or ".venv" in root or "graphify-out" in root:
            continue
        for file in files:
            ext = os.path.splitext(file)[1].lower()
            if ext in ['.tex', '.md', '.html', '.txt', '.py', '.json']:
                full_path = os.path.join(root, file)
                update_file(full_path)

if __name__ == '__main__':
    main()
