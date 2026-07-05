#!/bin/bash
# Fetch Google Scholar stats from this machine (GitHub runners get 403'd by
# Google) and push _data/scholar.json if the numbers changed.
# Scheduled every 3 days via ~/Library/LaunchAgents/com.lilytan.scholar-update.plist
set -u
REPO="/Users/lillychen/YalingTan678.github.io"
URL="https://scholar.google.com/citations?user=_BC9GucAAAAJ&hl=en"
UA="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"

cd "$REPO" || exit 1
git pull --rebase --quiet origin master 2>/dev/null

nums=$(curl -s --max-time 30 -A "$UA" "$URL" | grep -o '<td class="gsc_rsb_std">[0-9]*</td>' | grep -o '[0-9]*')
count=$(echo "$nums" | grep -c .)
if [ "$count" -lt 6 ]; then
  echo "$(date): fetch failed (got $count numbers), keeping existing file" >> /tmp/scholar-update.log
  exit 0
fi

set -- $nums
cat > _data/scholar.json <<JSON
{
  "citations_all": $1,
  "citations_recent": $2,
  "h_index_all": $3,
  "h_index_recent": $4,
  "i10_index_all": $5,
  "i10_index_recent": $6
}
JSON

if git diff --quiet _data/scholar.json; then
  echo "$(date): no change (citations=$1)" >> /tmp/scholar-update.log
  exit 0
fi

git add _data/scholar.json
git commit --quiet -m "chore: update Google Scholar stats (citations $1, h-index $3)"
git pull --rebase --quiet origin master
git push --quiet origin master
echo "$(date): pushed update (citations=$1, h-index=$3)" >> /tmp/scholar-update.log
