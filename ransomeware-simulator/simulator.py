import argparse
import os
from config import VICTIM_DIR
from utils.faux_locker import lock_file, unlock_all
from utils.ransom_note import drop_note


def init_victim_files(count=5):
    """Creates dummy victim files."""
    if not os.path.exists(VICTIM_DIR):
        os.makedirs(VICTIM_DIR)

    for i in range(count):
        filepath = os.path.join(VICTIM_DIR, f"file_{i}.txt")
        with open(filepath, "w") as f:
            f.write(f"This is victim file {i}\n")
    print(f"[+] Created {count} victim files at {VICTIM_DIR}")


def encrypt_files():
    """Simulates encryption."""
    for filename in os.listdir(VICTIM_DIR):
        filepath = os.path.join(VICTIM_DIR, filename)
        if os.path.isfile(filepath) and not filepath.endswith(".locked"):
            lock_file(filepath)
    drop_note()


def decrypt_files():
    """Simulates decryption."""
    unlock_all()


def main():
    parser = argparse.ArgumentParser(description="Fake Ransomware Simulator")
    parser.add_argument("action", choices=["init", "lock", "unlock"], help="Action to perform")
    parser.add_argument("--count", type=int, default=5, help="Number of files to create (for init)")

    args = parser.parse_args()

    if args.action == "init":
        init_victim_files(args.count)
    elif args.action == "lock":
        encrypt_files()
    elif args.action == "unlock":
        decrypt_files()


if __name__ == "__main__":
    main()
