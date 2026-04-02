"""Fetch Google Scholar citation stats and save to _data/scholar.json."""

import json
import re
import sys
import urllib.request
from pathlib import Path

SCHOLAR_ID = "_BC9GucAAAAJ"
URL = f"https://scholar.google.com/citations?user={SCHOLAR_ID}&hl=en"

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/124.0.0.0 Safari/537.36"
    ),
    "Accept-Language": "en-US,en;q=0.9",
}

OUT = Path(__file__).resolve().parent.parent / "_data" / "scholar.json"


def fetch():
    req = urllib.request.Request(URL, headers=HEADERS)
    with urllib.request.urlopen(req, timeout=30) as resp:
        return resp.read().decode("utf-8")


def parse(html: str) -> dict:
    # The stats table has cells: Citations, h-index, i10-index (All / Since 5yr)
    # Pattern: <td class="gsc_rsb_std">NUMBER</td>
    nums = re.findall(r'<td class="gsc_rsb_std">(\d+)</td>', html)
    if len(nums) < 4:
        raise ValueError(f"Could not parse stats (found {len(nums)} numbers)")
    return {
        "citations_all": int(nums[0]),
        "citations_recent": int(nums[1]),
        "h_index_all": int(nums[2]),
        "h_index_recent": int(nums[3]),
        "i10_index_all": int(nums[4]) if len(nums) > 4 else 0,
        "i10_index_recent": int(nums[5]) if len(nums) > 5 else 0,
    }


def main():
    try:
        html = fetch()
        stats = parse(html)
    except Exception as e:
        print(f"⚠ Failed to fetch live stats: {e}", file=sys.stderr)
        # Keep existing file if fetch fails
        if OUT.exists():
            print("Keeping existing scholar.json")
            return
        # Write defaults so the site still builds
        stats = {
            "citations_all": 0,
            "citations_recent": 0,
            "h_index_all": 0,
            "h_index_recent": 0,
            "i10_index_all": 0,
            "i10_index_recent": 0,
        }

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(stats, indent=2) + "\n")
    print(f"✓ Updated {OUT}: {stats}")


if __name__ == "__main__":
    main()
