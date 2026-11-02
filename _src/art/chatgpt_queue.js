/* ChatGPT 网页内自动出图队列（在 chatgpt.com 对话页里用 javascript_exec 执行）。
   用法：先定义 window.__Q = [[编号, 提示词], ...]（提示词以〔编号〕开头），再执行本文件内容，最后执行
   window.__R.log.push(window.__Q[0][0]+' sent '+(await window.__send(window.__Q[0][1])));
   每张图出完后自动下载为 window.__PREFIX + 编号 + '.png'（默认 numgate_），并自动发下一条。
   查看进度：JSON.stringify(window.__R.log)。出完会记录 'ALL DONE'。
   原理：按“该〔编号〕那条消息之后出现的图”取图，不靠图片地址判重（ChatGPT 对话是虚拟滚动，旧图会重新进画面）。 */
(()=>{
const busy=()=>[...document.querySelectorAll('button')].some(b=>b.getAttribute('aria-label')==='Stop');
window.__PREFIX=window.__PREFIX||'numgate_';
window.__send=async t=>{const el=document.querySelector('.ProseMirror');el.focus();document.execCommand('selectAll');document.execCommand('insertText',false,t);await new Promise(r=>setTimeout(r,800));const b=[...document.querySelectorAll('button')].find(b=>/^Send/.test(b.getAttribute('aria-label')||''));if(b){b.click();return true}return false};
window.__dlImg=async(im,name)=>{const c=document.createElement('canvas');c.width=im.naturalWidth;c.height=im.naturalHeight;c.getContext('2d').drawImage(im,0,0);const b=await new Promise(r=>c.toBlob(r,'image/png'));const a=document.createElement('a');a.href=URL.createObjectURL(b);a.download=name;document.body.appendChild(a);a.click();a.remove();return b.size};
const tokNode=tok=>{const w=document.createTreeWalker(document.querySelector('main'),NodeFilter.SHOW_TEXT);let n,last=null;while(n=w.nextNode()){if(n.nodeValue.includes(tok))last=n}return last};
const after=tok=>{const t=tokNode(tok);if(!t)return [];return [...document.querySelectorAll('main img')].filter(i=>i.naturalWidth>300&&/Generated image/.test(i.alt)&&(t.compareDocumentPosition(i)&Node.DOCUMENT_POSITION_FOLLOWING))};
clearInterval(window.__T);
window.__R={i:0,cur:window.__Q[0][0],log:[],idle:0,retry:0,lock:0,done:0};
window.__T=setInterval(async()=>{const R=window.__R;if(R.done||R.lock)return;if(busy()){R.idle=0;return}R.idle+=5;
 const sc=document.querySelector('main [class*="overflow-y-auto"]');if(sc)sc.scrollTop=sc.scrollHeight;
 const nw=after('〔'+R.cur+'〕');
 if(nw.length){R.lock=1;try{await new Promise(r=>setTimeout(r,2500));const im=after('〔'+R.cur+'〕').pop();const sz=await window.__dlImg(im,window.__PREFIX+R.cur+'.png');R.log.push(R.cur+' ok '+sz+' '+im.naturalWidth+'x'+im.naturalHeight);R.i++;R.retry=0;if(R.i>=window.__Q.length){R.done=1;R.log.push('ALL DONE')}else{R.cur=window.__Q[R.i][0];await new Promise(r=>setTimeout(r,1500));R.log.push(R.cur+' sent '+(await window.__send(window.__Q[R.i][1])));R.idle=0}}finally{R.lock=0}return}
 if(R.idle>=60){R.lock=1;try{R.retry++;if(R.retry>3){R.done=1;R.log.push(R.cur+' FAILED 3x');return}R.log.push(R.cur+' retry '+R.retry+' '+(await window.__send('〔'+R.cur+'〕请直接把这一张画出来：'+window.__Q[R.i][1].replace(/^〔[^〕]*〕/,''))));R.idle=0}finally{R.lock=0}}
},5000);
})();
