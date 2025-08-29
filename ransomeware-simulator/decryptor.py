# Thin wrapper to run the safe restore routine
from utils.faux_locker import unlock_all
from utils.lab_logger import LabLogger
from config import LOG_DIR

if __name__ == "__main__":
    logger = LabLogger(LOG_DIR/"simulator.log", LOG_DIR/"events.jsonl")
    restored = unlock_all()
    logger.log("restore", f"Restore invoked via decryptor.py: {restored} files.", status="success")
    print(f"[decryptor] Restored {restored} files.")
