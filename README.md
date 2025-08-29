# 🕵️ Fake Ransomware Simulator  

A **safe educational project** that simulates how ransomware behaves in a controlled environment.  
⚠️ **Note:** This is for **learning and awareness only**. It does **not** contain any malicious code that harms your system.  
---
## 📌 Features
- Creates dummy "victim files" filled with text data.  
- Simulates **encryption** by renaming files and adding a `.locked` extension.  
- Drops a **fake ransom note** into the victim folder.  
- Allows you to "decrypt" and restore the files.  
---

## 🛠️ Project Structure
ransomware-simulator/
│
├── simulator.py           # CLI control panel (init/start/status/restore/clean)
├── decryptor.py           # Thin wrapper that calls restore
├── config.py              # Safety config (lab root, paths, extensions)
├── utils/
│   ├── file_scanner.py
│   ├── faux_locker.py     # SAFE: base64 “lock” + move originals to backup
│   ├── ransom_note.py
│   ├── lab_logger.py
│   ├── integrity.py
├── victim_files/          # Populated by `init`
├── backups/               # Originals moved here during “start”
├── logs/                  # Text + JSONL logs
└── README.md


---

## 🚀 Getting Started  

### 1️⃣ Clone the repository
```bash
git clone https://github.com/Leevan-Michael/ransomware-simulator.git
cd ransomware-simulator

### 2️⃣ Run the simulator
```bash
python3 simulator.py init --count 10

