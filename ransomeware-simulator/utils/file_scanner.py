from pathlib import Path
from typing import List
from . import integrity
from config import LAB_ROOT, VICTIM_DIR, REFUSE_OUTSIDE_LAB, TARGET_EXTENSIONS, SIM_MARKER


def _is_inside(child: Path, parent: Path) -> bool:
    try:
        child.resolve().relative_to(parent.resolve())
        return True
    except Exception:
        return False


def _has_sim_marker(p: Path) -> bool:
    marker = p.with_name(p.name + f".{SIM_MARKER}")
    return marker.exists()


def scan_targets() -> List[Path]:
    """
    SAFE SCAN: only files created by the simulator (carry .simcreated marker)
    and only within the hardcoded VICTIM_DIR, with target extensions.
    """
    if REFUSE_OUTSIDE_LAB and not _is_inside(VICTIM_DIR, LAB_ROOT):
        raise RuntimeError("Victim directory is not strictly inside lab root. Aborting.")
    targets: List[Path] = []
    if not VICTIM_DIR.exists():
        return targets

    for p in VICTIM_DIR.rglob("*"):
        if p.is_file() and p.suffix.lower() in TARGET_EXTENSIONS and _has_sim_marker(p):
            targets.append(p)
    return targets
