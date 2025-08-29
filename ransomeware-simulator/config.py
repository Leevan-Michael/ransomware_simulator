import os

# Directory where "victim" files are stored
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
VICTIM_DIR = os.path.join(BASE_DIR, "victim_files")

# Backup dir for "encrypted" files
BACKUP_DIR = os.path.join(BASE_DIR, "backup")

# Fake locked extension
LOCKED_EXT = ".locked"

# Manifest to track files
MANIFEST = os.path.join(BASE_DIR, "manifest.txt")

# Ransom note file
RANSOM_NOTE = "README_RESTORE_FILES.txt"
