// Cloudflare Pages：Supabase 转发口。国内部分网络直连 *.supabase.co 会被拦，
// 游戏在自有域名下改走 https://<本站>/sb/...，由这里转给 Supabase（只放行登录 auth 和数据 rest 两类接口）。
const UP = 'https://rsnucakekepfavknkqpj.supabase.co';
const DROP = ['host', 'cf-connecting-ip', 'cf-ipcountry', 'cf-ray', 'cf-visitor', 'x-forwarded-proto', 'x-real-ip', 'cookie'];
export async function onRequest({ request }) {
  const u = new URL(request.url);
  const path = u.pathname.replace(/^\/sb/, '');
  if (!/^\/(auth|rest)\/v1\//.test(path)) return new Response('not found', { status: 404 });
  const h = new Headers(request.headers);
  for (const k of DROP) h.delete(k);
  const hasBody = !['GET', 'HEAD'].includes(request.method);
  const r = await fetch(UP + path + u.search, {
    method: request.method,
    headers: h,
    body: hasBody ? await request.arrayBuffer() : undefined,
    redirect: 'manual',
  });
  const rh = new Headers(r.headers);
  rh.delete('set-cookie');
  rh.set('cache-control', 'no-store');
  return new Response(r.body, { status: r.status, headers: rh });
}
