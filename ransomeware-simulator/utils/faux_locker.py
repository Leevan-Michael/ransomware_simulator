import os
import shutil
from config import BACKUP_DIR, LOCKED_EXT, MANIFEST, VICTIM_DIR


def lock_file(filepath):
    """Simulates encrypting a file by renaming & backing it up."""
    if not os.path.exists(BACKUP_DIR):
        os.makedirs(BACKUP_DIR)

    filename = os.path.basename(filepath)
    backup_path = os.path.join(BACKUP_DIR, filename)

    # Backup original
    shutil.copy2(filepath, backup_path)

    # Rename with .locked extension
    locked_path = filepath + LOCKED_EXT
    os.rename(filepath, locked_path)

    with open(MANIFEST, "a") as mf:
        mf.write(filepath + "\n")

    print(f"[+] Locked {filepath}")


def unlock_all():
    """Simulates decryption by restoring files from backup."""
    if not os.path.exists(MANIFEST):
        print("[-] No manifest found, nothing to unlock.")
        return

    with open(MANIFEST, "r") as mf:
        files = mf.read().splitlines()

    for filepath in files:
        locked_path = filepath + LOCKED_EXT
        backup_file = os.path.join(BACKUP_DIR, os.path.basename(filepath))

        if os.path.exists(backup_file):
            shutil.copy2(backup_file, filepath)
            if os.path.exists(locked_path):
                os.remove(locked_path)
            print(f"[+] Restored {filepath}")

    os.remove(MANIFEST)
    print("[+] All files unlocked.")
