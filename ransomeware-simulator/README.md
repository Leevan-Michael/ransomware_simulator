# SAFE Ransomware Training Simulator (Non-Destructive)

This project **does not** encrypt real files and **cannot** operate outside its lab folder.
It is intended for training incident response workflows, SIEM log parsing, and tabletop drills.

## Safety Guarantees
- Works only on dummy files created by `init`.
- Refuses to scan outside the fixed `victim_files/` directory.
- “Locks” by moving originals to `backups/` and writing decoy `.locked` files containing base64 + metadata.
- Full restore is always available.

## Quickstart
```bash
python simulator.py init --count 15
python simulator.py start
python simulator.py status
python simulator.py restore
python simulator.py clean
