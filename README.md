# 御剑斩妖录 / 星愿魔法少女

朋友之间玩的修仙数字门小游戏。用昵称 + 密码注册登录，存档跟着账号走，每局结束可以看排行榜。

- 游戏：`index.html`（单文件，GitHub Pages 直接托管）
- 后台：Supabase（`supabase.sql` 是建表语句，`config.json` 里是公开的项目地址和 anon key）
- `.github/workflows/keepalive.yml`：每 3 天访问一次数据库，防止免费项目被自动暂停
