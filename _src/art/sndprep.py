#!/usr/bin/env python3
"""11-02 18:40 John：合成音效听着 low → 换成真实录制的 CC0 音效（Kenney 系列 + wyzowl/sfx-kit，均 CC0）。
把选定的源文件裁剪、淡出、转单声道 mp3，输出 art/out/sx_<事件>.mp3（修仙版）、art/out/g_sx_<事件>.mp3（女生版）。"""
import subprocess,os,glob
S='/tmp/claude-0/pt/snd/'
K=S+'kenney-impact-sounds-for-godot/'; KF=lambda n:glob.glob(K+'**/'+n+'.ogg',recursive=True)[0]
KA=lambda pat:sorted(glob.glob(S+'**/'+pat,recursive=True))[0]
X=S+'sfx-kit/sounds/'
OUT='/home/claude/numgate/art/out/'
# 事件: (修仙版源, 女生版源, 最长秒数, 音量dB)
M={
 'kill':(KA('impact_wood_light_002.ogg'),X+'pops/pop-small-bubble.wav',.35,-4),
 'coin':(X+'money/money-coin-drop.wav',X+'money/money-coin-drop.wav',.5,-8),
 'gate_good':(X+'shimmers/shimmer-short-bright.wav',X+'shimmers/shimmer-short-sparkle.wav',1.0,-3),
 'gate_bad':(X+'notifications/notification-failure-thud.wav',X+'notifications/notification-failure-wobble.wav',1.0,-2),
 'unlock':(KA('metal_latch*.ogg'),X+'appear-and-vanish/appear-burst.wav',1.0,-2),
 'deny':(X+'notifications/notification-failure-knock.wav',X+'notifications/notification-failure-knock.wav',.6,-6),
 'up':(X+'logo-stings/sting-warm-short.wav',X+'logo-stings/sting-playful-short.wav',1.6,-4),
 'pick':(X+'tones/tone-ding-high.wav',X+'tones/tone-ding-high.wav',.8,-6),
 'buy':(X+'money/money-coin-stack.wav',X+'money/money-coin-stack.wav',1.0,-4),
 'realm':(KA('impact_bell_heavy_000.ogg'),X+'celebration/celebration-confetti.wav',2.5,0),
 'realm2':(X+'logo-stings/sting-bold-long.wav',X+'logo-stings/sting-bright-long.wav',3.0,-3),
 'brk_ready':(X+'shimmers/shimmer-medium-bright.wav',X+'shimmers/shimmer-medium-sparkle.wav',1.5,-4),
 'evolve':(X+'logo-stings/sting-warm-long.wav',X+'logo-stings/sting-playful-long.wav',2.5,-3),
 'hurt':(KA('impact_punch_medium_000.ogg'),X+'impacts/impact-light-soft.wav',.5,-3),
 'breach':(X+'impacts/impact-heavy-hard.wav',X+'impacts/impact-heavy-firm.wav',1.2,0),
 'drain':(X+'notifications/notification-failure-deflate.wav',X+'notifications/notification-failure-deflate.wav',1.0,-3),
 'boss':(X+'cinematic-hits/cinematic-drum-massive.wav',X+'booms-and-bass/boom-drop-soft.wav',2.5,0),
 'surge':(X+'cinematic-hits/cinematic-drum-big.wav',X+'risers-and-fallers/riser-1s-soft.wav',2.2,-1),
 'calm':(X+'logo-stings/sting-minimal-short.wav',X+'shimmers/shimmer-medium-soft.wav',1.6,-4),
 'warn':(X+'risers-and-fallers/riser-2s-strong.wav',X+'risers-and-fallers/riser-2s-soft.wav',2.0,-3),
 'curse':(X+'risers-and-fallers/faller-1s-soft.wav',X+'risers-and-fallers/faller-1s-soft.wav',1.0,-4),
 'interrupt':(KA('impact_metal_heavy_000.ogg'),KA('impact_glass_heavy_000.ogg'),.8,-2),
 'gourd':(X+'appear-and-vanish/appear-dissolve.wav',X+'money/money-coins-pour.wav',1.2,-3),
 'bell':(KA('impact_bell_heavy_002.ogg'),X+'tones/tone-ding-low.wav',2.0,-2),
 'shell':(X+'impacts/impact-light-firm.wav',X+'pops/pop-medium-out.wav',.4,-10),
 'card':(KA('book_flip*.ogg'),KA('book_flip*.ogg'),.8,-4),
 'shield':(KA('force_field_000.ogg'),X+'appear-and-vanish/appear-materialise.wav',1.5,-3),
 'freeze':(KA('impact_glass_heavy_001.ogg'),X+'shimmers/shimmer-long-sparkle.wav',1.8,-3),
 'mana':(X+'notifications/notification-error-soft.wav',X+'notifications/notification-error-soft.wav',.6,-8),
 'fire_cast':(X+'whooshes/whoosh-fast-medium.wav',X+'swishes-and-zips/swish-medium.wav',.7,-4),
 'fire_hit':(X+'booms-and-bass/boom-hit-medium.wav',X+'appear-and-vanish/appear-poof.wav',1.2,-2),
 'ice':(KA('impact_glass_medium_000.ogg'),X+'shimmers/shimmer-short-sparkle.wav',1.2,-3),
 'sword':(KA('draw_knife*.ogg'),X+'swishes-and-zips/swish-hard.wav',.9,-2),
 'sword2':(X+'whooshes/whoosh-fast-hard.wav',X+'shimmers/shimmer-short-bright.wav',.8,-4),
 'crow':(X+'whooshes/whoosh-fast-soft.wav',X+'swishes-and-zips/zip-in-soft.wav',.5,-10),
 'zap':(KA('zap1.ogg') if glob.glob(S+'**/zap1.ogg',recursive=True) else KA('zap*.ogg'),X+'shimmers/shimmer-short-sparkle.wav',.6,-8),
 'orb':(KA('impact_glass_light_000.ogg'),X+'pops/pop-small-in.wav',.4,-12),
 'pet':(KA('impact_soft_medium_000.ogg'),X+'pops/pop-medium-out.wav',.5,-8),
 'wan':(X+'whooshes/whoosh-medium-hard.wav',X+'swishes-and-zips/zip-out-hard.wav',.9,-4),
 'bomb':(X+'cinematic-hits/cinematic-thunder-massive.wav',X+'celebration/celebration-fireworks.wav',3.0,0),
 'bolt':(X+'cinematic-hits/cinematic-thunder-big.wav',X+'shimmers/shimmer-long-bright.wav',2.2,-1),
 'death':(X+'risers-and-fallers/faller-2s-strong.wav',X+'risers-and-fallers/faller-2s-soft.wav',2.2,-1),
 'cut':(X+'whooshes/whoosh-medium-hard.wav',X+'whooshes/whoosh-medium-soft.wav',.9,-2),
 'jar':(X+'shimmers/shimmer-medium-bright.wav',X+'celebration/celebration-popper.wav',1.5,-3),
}
for ev,(a,b,mx,db) in M.items():
    for src,pre in ((a,''),(b,'g_')):
        o=OUT+pre+'sx_'+ev+'.mp3';fo=max(.05,min(.3,mx*.25))
        r=subprocess.run(['ffmpeg','-i',src,'-t',str(mx),'-af','silenceremove=start_periods=1:start_threshold=-50dB,volumedetect','-f','null','-'],capture_output=True,text=True).stderr
        import re;pk=float(re.search(r'max_volume: ([-0-9.]+)',r).group(1));g=(-1.5-pk)+db   # 先把峰值统一到 -1.5 dB，再按事件减音量
        subprocess.run(['ffmpeg','-y','-loglevel','error','-i',src,'-t',str(mx),'-ac','1','-ar','32000','-af','silenceremove=start_periods=1:start_threshold=-50dB,volume=%.1fdB,afade=t=out:st=%s:d=%s'%(g,max(0,mx-fo),fo),'-b:a','64k',o],check=True)
tot=sum(os.path.getsize(f) for f in glob.glob(OUT+'*sx_*.mp3'));print(len(M),'events',tot//1024,'KB')
