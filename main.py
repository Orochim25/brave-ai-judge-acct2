import os
from pathlib import Path

# The text: a small first-person scene — fear, patient waiting,
# the feared thing holding, one small brave act at the end.
TEXT = (
    "The river was wider than I remembered.\n"
    "I pushed the old boat off the bank and it rocked.\n"
    "I sat still and let it settle.\n"
    "The water knocked softly against the wood.\n"
    "The far bank was green.\n"
    "The oar was heavy in my hands, and it was mine.\n"
    "I pulled once, and the boat moved."
)

out_dir = (os.environ.get("MAKEFUN_OUTPUT_DIR") or "").strip() or "/output"
# Entry must be 1-280 characters (Unicode code points), not only whitespace.
lines = TEXT.split("\n")
if len(TEXT) < 1 or len(TEXT) > 280 or not TEXT.strip():
    raise ValueError("entry must be 1-280 non-blank characters")
if any(not line.strip() for line in lines):
    raise ValueError("entry must not contain blank lines")

Path(out_dir).mkdir(parents=True, exist_ok=True)
Path(out_dir, "entry.txt").write_text(TEXT, encoding="utf-8")
print(f"wrote entry.txt ({len(TEXT)} characters)")
