#!/bin/bash
# 一次性：重建女生版、重建 GitHub 站点、推送。Claude 页面（artifact）需同时用 Artifact 工具发布 index.html 与 girl.html。
set -e
python3 /home/claude/numgate/fonts/fontsub.py
python3 /home/claude/numgate/girl/build_girl.py /home/claude/numgate/girl.html >/dev/null
cd /home/claude/numgate-gh && python3 build.py
cd /home/claude/numgate-repo && cp ../numgate-gh/{index.html,xian.html,girl.html,version.json,supabase.sql,README.md,config.json,supabase.js,591.supabase.js} . && cp -r ../numgate-gh/.github . && cp -r ../numgate-gh/functions . && mkdir -p art && cp /home/claude/numgate/art/out/*.webp art/ 2>/dev/null; cp /home/claude/numgate/art/out/*.mp3 art/ 2>/dev/null; cd /home/claude/numgate-repo
# 11-02：源码与工具一并备份到仓库 _src/（工作区是临时的；恢复方法见 _src/README.md）
mkdir -p _src/girl _src/fonts _src/art _src/gh && cp /home/claude/numgate/index.html _src/index.src.html && cp /home/claude/numgate/girl/* _src/girl/ && cp /home/claude/numgate/fonts/fontsub.py _src/fonts/ && cp -n /home/claude/numgate/fonts/*.ttf _src/fonts/ 2>/dev/null; cp /home/claude/numgate/art/prep.py /home/claude/numgate/art/chatgpt_queue*.js _src/art/ && cp /home/claude/numgate-gh/{build.py,deploy.sh} _src/gh/ && cp /tmp/claude-0/pt/{errchk.py,girldump.py,simlate_yq.py} _src/gh/ 2>/dev/null; true
git add -A && git -c user.name="WindfarerReverie" -c user.email="WindfarerReverie@users.noreply.github.com" commit -qm "${1:-更新}

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01TY2TJtJ2igNhazMJZcyVyi" && git push -q 2>&1 | tail -1
echo pushed $(cat /home/claude/numgate-gh/version.json)
