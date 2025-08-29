import json
from datetime import datetime
from pathlib import Path
from typing import Dict, Any

class LabLogger:
    def __init__(self, text_log: Path, jsonl_log: Path):
        self.text_log = text_log
        self.jsonl_log = jsonl_log
        self.text_log.parent.mkdir(parents=True, exist_ok=True)
        self.jsonl_log.parent.mkdir(parents=True, exist_ok=True)

    def _ts(self) -> str:
        return datetime.utcnow().isoformat(timespec="seconds") + "Z"

    def log(self, action: str, detail: str, extra: Dict[str, Any] = None, status: str = "info"):
        line = f"[{self._ts()}] [{status.upper()}] {action}: {detail}"
        with self.text_log.open("a", encoding="utf-8") as f:
            f.write(line + "\n")
        rec = {"timestamp": self._ts(), "action": action, "detail": detail, "status": status}
        if extra:
            rec.update(extra)
        with self.jsonl_log.open("a", encoding="utf-8") as f:
            f.write(json.dumps(rec, ensure_ascii=False) + "\n")
