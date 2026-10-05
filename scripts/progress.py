"""
Progress dashboard. Run: python scripts/progress.py

Batata hai: current streak, total active days, daily logs, DSA solved,
[ai] commits ka ratio. Sab git history aur files se, koi manual entry nahi.
"""
import subprocess
from datetime import date, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def git_lines(*args: str) -> list[str]:
    try:
        out = subprocess.run(["git", *args], cwd=ROOT, capture_output=True, text=True, check=True)
    except (subprocess.CalledProcessError, FileNotFoundError):
        return []
    return [line for line in out.stdout.splitlines() if line.strip()]


def commit_dates() -> set[date]:
    return {date.fromisoformat(d) for d in git_lines("log", "--format=%ad", "--date=short")}


def current_streak(days: set[date], today: date) -> int:
    # Aaj abhi commit nahi kiya to kal se gino (streak tab tak zinda hai)
    day = today if today in days else today - timedelta(days=1)
    streak = 0
    while day in days:
        streak += 1
        day -= timedelta(days=1)
    return streak


def longest_streak(days: set[date]) -> int:
    best = run = 0
    prev = None
    for d in sorted(days):
        run = run + 1 if prev and d - prev == timedelta(days=1) else 1
        best = max(best, run)
        prev = d
    return best


def main() -> None:
    days = commit_dates()
    messages = git_lines("log", "--format=%s")
    ai_commits = sum("[ai]" in m.lower() for m in messages)
    logs = [p for p in (ROOT / "daily-log").glob("day*.md")]
    dsa = [p for p in (ROOT / "dsa").rglob("*.py") if p.name != "__init__.py"]
    recall = [p for p in (ROOT / "recall").glob("*.py")]

    total = len(messages)
    ai_pct = (ai_commits / total * 100) if total else 0

    print("=" * 40)
    print(f"  Current streak   : {current_streak(days, date.today())} din")
    print(f"  Longest streak   : {longest_streak(days)} din")
    print(f"  Active days      : {len(days)}")
    print(f"  Daily logs       : {len(logs)} / 42")
    print(f"  DSA solved       : {len(dsa)}")
    print(f"  Recall drills    : {len(recall)}")
    print(f"  Commits          : {total}  ([ai] = {ai_commits}, {ai_pct:.0f}%)")
    print("=" * 40)
    if ai_pct > 30:
        print("  Warning: 30% se zyada commits AI-assisted hain. Khud likh.")


if __name__ == "__main__":
    main()
