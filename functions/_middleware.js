// Cloudflare Pages：按子域名直接打开对应版本（xian.youfeng.app → 修仙版，xingyuan.youfeng.app → 女生版）
export async function onRequest(ctx){
  const u=new URL(ctx.request.url),h=u.hostname,p=u.pathname;
  if(p==='/'||p==='/index.html'||p==='/index'){
    const page=h.startsWith('xian.')?'/xian':h.startsWith('xingyuan.')?'/girl':null;
    if(page){const r=await ctx.env.ASSETS.fetch(new URL(page,u.origin));
      return new Response(r.body,{status:200,headers:{'content-type':'text/html; charset=utf-8','cache-control':'no-cache'}})}
  }
  return ctx.next();
}
