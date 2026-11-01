-- 御剑斩妖录 / 星愿魔法少女 · 后台数据库（在 Supabase 的 SQL Editor 里整段粘贴，点 Run）
-- ver = 'xian'（修仙版）或 'girl'（女生版），两个版本的存档和排行榜分开

create table if not exists public.saves (
  id uuid not null references auth.users(id) on delete cascade,
  ver text not null default 'xian',
  data jsonb not null default '{}'::jsonb,
  updated_at timestamptz not null default now(),
  primary key (id, ver)
);
alter table public.saves enable row level security;
create policy "own save read"   on public.saves for select to authenticated using (id = auth.uid());
create policy "own save insert" on public.saves for insert to authenticated with check (id = auth.uid());
create policy "own save update" on public.saves for update to authenticated using (id = auth.uid()) with check (id = auth.uid());

create table if not exists public.scores (
  id uuid not null references auth.users(id) on delete cascade,
  ver text not null default 'xian',
  slot int not null check (slot between 1 and 3),
  name text not null check (char_length(name) between 1 and 16),
  best_realm int not null default 0,
  best_wave int not null default 0,
  clears int not null default 0,
  best_clear int,
  score int not null default 0,
  life int not null default 1,
  updated_at timestamptz not null default now(),
  primary key (id, ver, slot)
);
alter table public.scores enable row level security;
create policy "scores read all" on public.scores for select to anon, authenticated using (true);
create policy "own score insert" on public.scores for insert to authenticated with check (id = auth.uid());
create policy "own score update" on public.scores for update to authenticated using (id = auth.uid()) with check (id = auth.uid());

grant select, insert, update on public.saves to authenticated;
grant select on public.scores to anon, authenticated;
grant insert, update on public.scores to authenticated;
