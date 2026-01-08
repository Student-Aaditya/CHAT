# RAG/routers/event_router.py
import json, os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

# -------------- LOAD DATA (SAME FILE) --------------
with open("RAG/data/event_chunks.json", "r", encoding="utf-8") as f:
    DATA = json.load(f)


def event_normalize(q: str) -> str:
    q = q.lower().strip()
    for ch in ["?", ",", ".", ":", "-"]:
        q = q.replace(ch, " ")
    return " ".join(q.split())


def event_router(query: str):
    q = event_normalize(query)

    for item in DATA:
        if item.get("category") != "event":
            continue

        name = item.get("event_name", "").lower()
        if name and (q == name or q in name or name in q):
            return item.get("answer")

    for item in DATA:
        if item.get("category") != "event":
            continue

        for kw in item.get("keywords", []):
            if kw.lower() in q.split():
                return item.get("answer")

    if any(w in q for w in ["event", "events", "happening", "happenings", "news"]):
        events = [
            "• " + e.get("event_name")
            for e in DATA
            if e.get("category") == "event" and e.get("event_name")
        ]

        if events:
            return (
                "Recent Events & Happenings at NIET\n\n"
                + "\n".join(events)
            )

    return None


if __name__ == "__main__":
    tests = [
        "niet events",
        "latest happenings",
        "alumni talk",
        "hackathon",
        "ieee conference"
    ]

    for t in tests:
        print("Q:", t)
        print(event_router(t))
        print("-" * 40)
