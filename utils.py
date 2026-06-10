from pathlib import Path

def load_completed():
    completed = set()

    if Path("completed.txt").exists():
        with open("completed.txt", "r", encoding="utf-8") as f:
            completed = set(line.strip() for line in f)

    return completed


def save_completed(url):
    with open("completed.txt", "a", encoding="utf-8") as f:
        f.write(url + "\n")


def save_failed(url):
    with open("failed.txt", "a", encoding="utf-8") as f:
        f.write(url + "\n")
