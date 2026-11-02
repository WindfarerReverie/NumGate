# 源码与构建工具备份（游戏不读取本目录）

工作区是临时的，这里是重建工作环境用的完整源码。每次 deploy.sh 自动同步。

恢复步骤（新工作区）：
1. 克隆本仓库到 /home/claude/numgate-repo；再复制一份站点文件到 /home/claude/numgate-gh（index.html 以外的 functions/、supabase.*、config.json、README.md、.github/）。
2. 建 /home/claude/numgate：
   - _src/index.src.html → numgate/index.html（主源文件，修仙版）
   - _src/girl/* → numgate/girl/（女生版：build_girl.py 替换表 + theme_girl.js/css + font_girl.css）
   - _src/fonts/* → numgate/fonts/（fontsub.py + 两个字体）
   - _src/art/* → numgate/art/（prep.py 素材处理；chatgpt_queue*.js 出图脚本）
   - 仓库 art/*.webp → numgate/art/out/（游戏用素材）；art_src/*.webp 是原图存档（原尺寸，质量 90）
   - _src/gh/build.py、deploy.sh → numgate-gh/
3. 发布：bash /home/claude/numgate-gh/deploy.sh "说明"，再用 Artifact 发布 numgate/index.html 与 numgate/girl.html。
4. 测试脚本（errchk.py / girldump.py / simlate_yq.py）放到 /tmp/claude-0/pt，并在该目录起 python3 -m http.server 8765；art/ 要复制一份到同目录。
