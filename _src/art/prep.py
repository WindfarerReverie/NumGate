#!/usr/bin/env python3
"""ChatGPT 出的素材 → 游戏用 webp。用法：python3 prep.py [源目录]
源文件名 numgate_<编号>.png；同一编号有 q 版（如 H4q）时优先用 q 版。
输出到本目录 out/，并写 out/manifest.json（游戏按需加载，没有的继续用代码画）。"""
import sys, os, json
from PIL import Image

SRC = sys.argv[1] if len(sys.argv) > 1 else '/mnt/user-data/uploads/Downloads'
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'out')
os.makedirs(OUT, exist_ok=True)

# 编号 → (输出名, 最长边像素)
MAP = {
    'H1': ('hero_ti_0', 300), 'H2': ('hero_ti_1', 300), 'H3': ('hero_ti_2', 300),
    'H4': ('hero_fa_0', 300), 'H5': ('hero_fa_1', 300), 'H6': ('hero_fa_2', 300),
    'P1': ('pet_0', 220), 'P2': ('pet_4', 220), 'P3': ('pet_6', 220),
    'P4': ('pet_1', 220), 'P5': ('pet_5', 220), 'P6': ('pet_11', 240),
    'M1': ('mon_n', 180), 'M2': ('mon_run', 180), 'M3': ('mon_brute', 200),
    'M4': ('mon_elite', 220), 'M5': ('mon_hex', 200), 'M6': ('mon_guard', 200),
    'B1': ('boss_3', 420), 'B2': ('boss_4', 420),
    'BG1': ('bg_cover', 1280), 'BG2': ('bg_r0', 1280), 'BG3': ('bg_r4', 1280),
    'H7': ('hero_ti_3', 300), 'H8': ('hero_ti_4', 300), 'H9': ('hero_fa_3', 300), 'H10': ('hero_fa_4', 300),
}
for i in list(range(0, 3)) + list(range(5, 18)):
    MAP['BS%d' % i] = ('boss_%d' % i, 420)
for i in [3] + list(range(5, 18)):
    MAP['BR%d' % i] = ('bg_r%d' % i, 1280)
for i in [2, 3, 7, 8, 9, 10, 12, 13, 14, 15, 16]:
    MAP['PF%d' % i] = ('pet_%d' % i, 240)
for t in ['n', 'run', 'brute', 'elite', 'hex', 'guard']:
    for b in range(1, 6):
        MAP['MV_%s_%d' % (t, b)] = ('mon_%s_%d' % (t, b), 220)
for i in range(1, 6):
    MAP['GH%d' % i] = ('g_hero_ti_%d' % (i - 1), 300)
    MAP['GH%d' % (i + 5)] = ('g_hero_fa_%d' % (i - 1), 300)
for i in range(1, 18):
    MAP['GP%d' % i] = ('g_pet_%d' % (i - 1), 240)
for i in range(18):
    MAP['GB%d' % i] = ('g_boss_%d' % i, 420)
for i, t in enumerate(['n', 'run', 'brute', 'elite', 'hex', 'guard']):
    MAP['GM%d' % (i + 1)] = ('g_mon_' + t, 200)
    for b in range(1, 6):
        MAP['GV_%s_%d' % (t, b)] = ('g_mon_%s_%d' % (t, b), 220)
MAP['GBGc'] = ('g_bg_cover', 1280)
MAP['SEAL'] = ('deco_seal', 96)
MAP['GSEAL'] = ('g_deco_seal', 96)
for p in ['ti', 'fa']:
    for r in range(1, 18):
        MAP['XR_%s_%d' % (p, r)] = ('hero_%s_r%d' % (p, r), 300)
        MAP['GHR_%s_%d' % (p, r)] = ('g_hero_%s_r%d' % (p, r), 300)
for i in range(1, 18):
    MAP['GFX%d' % i] = ('g_fx_%d' % i, 320)
for k in ['qi', 'vein', 'brk', 'xin', 'zou', 'art', 'fb', 'fu', 'jie', 'bomb', 'bolt', 'shield', 'freeze', 'fire', 'sword', 'ice', 'gourd', 'bell', 'mirror', 'crow', 'orb', 'cloud', 'gang', 'zhan', 'jj', 'mp', 'coin', 'heavy', 'lian', 'pojun', 'body', 'dmg', 'rate', 'spread', 'pierce', 'armor', 'cd', 'hp', 'sp', 't_armor', 't_guard', 't_swarm', 't_fast', 't_elite', 't_hex', 't_power']:
    MAP['GIC_' + k] = ('g_ic_' + k, 128)
for i in [0, 3, 6, 9, 12, 15]:
    MAP['GR%d' % i] = ('g_bg_r%d' % i, 1280)
for i in range(1, 18):
    MAP['FX%d' % i] = ('fx_%d' % i, 320)
for k in ['qi', 'vein', 'brk', 'xin', 'zou', 'art', 'fb', 'fu', 'jie', 'bomb', 'bolt', 'shield', 'freeze', 'fire', 'sword', 'ice', 'gourd', 'bell', 'mirror', 'crow', 'orb', 'cloud', 'mp', 'coin', 'gang', 'zhan', 'jj', 'heavy', 'lian', 'pojun', 'body', 'dmg', 'rate', 'spread', 'pierce', 'armor', 'cd', 'hp', 'sp', 't_armor', 't_guard', 't_swarm', 't_fast', 't_elite', 't_hex', 't_power']:
    MAP['IC_' + k] = ('ic_' + k, 128)

# 11-02 17:58：被动小伙伴（每个 4 个形态）+ 聚灵瓶 / 星光瓶
for k in ['crow', 'cloud', 'jj']:
    for n in range(1, 5):
        MAP['CMP_%s_%d' % (k, n)] = ('cmp_%s_%d' % (k, n), 260)
        MAP['GCMP_%s_%d' % (k, n)] = ('g_cmp_%s_%d' % (k, n), 260)
MAP['JAR'] = ('jar', 160)
for k in ['gourd', 'mirror', 'bell']:   # 11-02 18:35：法宝 / 魔法道具 4 个形态
    for n in range(1, 5):
        MAP['FB_%s_%d' % (k, n)] = ('cmp_fb_%s_%d' % (k, n), 220)
        MAP['GFB_%s_%d' % (k, n)] = ('g_cmp_fb_%s_%d' % (k, n), 220)
MAP['GJAR'] = ('g_jar', 160)
# 11-02 22:05 拖尾粒子、脚下光环、普通攻击弹道、三昧真火火柱
for k in ['cloud','sword','ink','peach','fire','frost','thunder','dragon']:
    MAP['TR_' + k] = ('tr_' + k, 96)
    MAP['GTR_' + k] = ('g_tr_' + k, 96)
for k in ['rune','taiji','lotus','sun']:
    MAP['AU_' + k] = ('au_' + k, 256)
    MAP['GAU_' + k] = ('g_au_' + k, 256)
for k in ['ti','fa']:
    MAP['PJ_' + k] = ('pj_' + k, 128)
    MAP['GPJ_' + k] = ('g_pj_' + k, 128)
MAP['XF_pillar'] = ('fx_pillar', 300)
# 11-02 23:08 全面美术自查：小兵、门框、锁、飞剑坐骑、光屑、冲击波、灵珠、阶数印记、树叶、剑罡/护盾光罩、战意/勇气火焰
for pre, gp in [('', ''), ('G', 'g_')]:
    for k in ['ti', 'fa']:
        MAP[pre + 'SQ_' + k] = (gp + 'sq_' + k, 64)
    MAP[pre + 'GATEF_good'] = (gp + 'gatef_good', 320)
    MAP[pre + 'GATEF_bad'] = (gp + 'gatef_bad', 320)
    MAP[pre + 'LOCK'] = (gp + 'lock', 64)
    MAP[pre + 'SPARK'] = (gp + 'spark', 64)
    MAP[pre + 'WAVE'] = (gp + 'wave', 320)
    MAP[pre + 'PORB'] = (gp + 'porb', 64)
    MAP[pre + 'PIP'] = (gp + 'pip', 48)
    for n in range(1, 5):
        MAP[pre + 'GANG_%d' % n] = (gp + 'gang_%d' % n, 300)
        MAP[pre + 'ZHAN_%d' % n] = (gp + 'zhan_%d' % n, 300)
MAP['XPLAT'] = ('xplat', 160)
MAP['DIV'] = ('div', 900)
MAP['GDIV'] = ('g_div', 900)
MAP['LEAF'] = ('leaf', 64)
# 11-03 15:12 新手任务卡上的动作小图标（代替表情符号）
for _n in ['tap','drag','lr','up','num','right','nocross','hourglass','target','refresh','break','scroll']:
    MAP['VI_' + _n] = ('vi_' + _n, 128)
    MAP['GVI_' + _n] = ('g_vi_' + _n, 128)
# 11-03 14:59 护山大阵 / 梦境结界（完好 + 破损两张，按气血交叉淡入）
for pre, gp in [('', ''), ('G', 'g_')]:
    MAP[pre + 'W1'] = (gp + 'ward', 900)
    MAP[pre + 'W2'] = (gp + 'ward_c', 900)
    MAP[pre + 'W3'] = (gp + 'ward_s', 900)   # 15:59 金钟罩 / 泡泡护盾加持版
# 11-03 16:57 体修爆发技光环（剑意沸腾 / 疾风连斩；女生版 勇气爆发 / 流星连射）
for pre, gp in [('', ''), ('G', 'g_')]:
    MAP[pre + 'BX1'] = (gp + 'aura_rage', 640)
    MAP[pre + 'BX2'] = (gp + 'aura_haste', 640)

def find(code):
    for c in (code + 'r', code + 'q', code):
        p = os.path.join(SRC, 'numgate_%s.png' % c)
        if os.path.exists(p):
            return p
    return None

def checker_fake(im):
    """RGB 图（没有真透明）或四角是灰白格子 → 视为不合格"""
    return im.mode != 'RGBA'

man = {}
for code, (name, M) in MAP.items():
    p = find(code)
    if not p:
        _o = os.path.join(OUT, name + '.webp')   # 11-02 18:12：源目录里没有这张时，保留已处理好的成品（否则换个源目录跑一次会把其他图全丢掉）
        if os.path.exists(_o):
            with Image.open(_o) as _w: man[name] = [_w.width, _w.height]
        continue
    _o = os.path.join(OUT, name + '.webp')
    if os.path.exists(_o) and os.path.getmtime(_o) > os.path.getmtime(p):   # 已处理过且源图没变：跳过（省时间）
        with Image.open(_o) as _w: man[name] = [_w.width, _w.height]
        continue
    im = Image.open(p)
    if code.startswith('BG') or code.startswith('BR') or code.startswith('GBG') or code.startswith('GR'):
        im = im.convert('RGB')
        im.thumbnail((M, M), Image.LANCZOS)
        im.save(os.path.join(OUT, name + '.webp'), 'WEBP', quality=80, method=6)
        man[name] = [im.width, im.height]
        print(code, os.path.basename(p), '->', name, im.size)
        continue
    if checker_fake(im):
        print(code, os.path.basename(p), 'SKIP: 没有透明通道')
        continue
    im = im.convert('RGBA')
    a = im.getchannel('A').point(lambda v: 0 if v < 14 else v)
    im.putalpha(a)
    box = a.point(lambda v: 255 if v > 40 else 0).getbbox()
    im = im.crop(box)
    im.thumbnail((M, M), Image.LANCZOS)
    im.save(os.path.join(OUT, name + '.webp'), 'WEBP', quality=86, method=6)
    man[name] = [im.width, im.height]
    print(code, os.path.basename(p), '->', name, im.size, os.path.getsize(os.path.join(OUT, name + '.webp')))

json.dump(man, open(os.path.join(OUT, 'manifest.json'), 'w'))
import hashlib, re
v = hashlib.md5(json.dumps(man, sort_keys=True).encode() + b''.join(open(os.path.join(OUT, k + '.webp'), 'rb').read() for k in sorted(man))).hexdigest()[:8]
ip = '/home/claude/numgate/index.html'
h = open(ip).read()
blk = '/*ARTMAN*/const ART_MAN=%s,ART_V=%r;/*ARTMAN_END*/' % (json.dumps({k: 1 for k in man}, separators=(',', ':')), v)
h2 = re.sub(re.escape('/*ARTMAN*/') + '.*?' + re.escape('/*ARTMAN_END*/'), lambda m: blk, h, flags=re.S)
assert h2 != h or blk in h
open(ip, 'w').write(h2)
print('total', len(man), sum(os.path.getsize(os.path.join(OUT, f)) for f in os.listdir(OUT)) // 1024, 'KB')
