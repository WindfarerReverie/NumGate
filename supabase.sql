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
-- 限量开放 + 排行榜防作弊（2026-11-01）
create table if not exists public.ng_config(k text primary key, v int not null);
insert into public.ng_config values('max_users',300) on conflict (k) do nothing;
alter table public.ng_config enable row level security;

create or replace function public.ng_cap() returns trigger language plpgsql security definer set search_path=public as $$
begin
  if (select count(*) from auth.users) >= (select v from public.ng_config where k='max_users') then
    raise exception 'NG_FULL';
  end if;
  return new;
end $$;
drop trigger if exists ng_cap on auth.users;
create trigger ng_cap before insert on auth.users for each row execute function public.ng_cap();

create or replace function public.ng_slots() returns json language sql security definer set search_path=public as $$
  select json_build_object('used',(select count(*) from auth.users),'max',(select v from public.ng_config where k='max_users'));
$$;
grant execute on function public.ng_slots() to anon, authenticated;

create or replace function public.ng_score_guard() returns trigger language plpgsql as $$
declare dt float;
begin
  new.updated_at := now();
  if new.name ~* '(傻逼|煞笔|操你|草泥马|fuck|shit|习近平|共产党|法轮)' then raise exception 'NG_NAME'; end if;
  if tg_op = 'INSERT' then
    if new.score > 30000 or new.best_realm > 60 then raise exception 'NG_CHEAT'; end if;
  else
    dt := greatest(1, extract(epoch from (now() - old.updated_at)));
    if new.clears <= old.clears and new.score - old.score > 300 + dt * 30 then raise exception 'NG_CHEAT'; end if;
    if new.best_realm - old.best_realm > 10 + dt / 30 then raise exception 'NG_CHEAT'; end if;
  end if;
  return new;
end $$;
drop trigger if exists ng_score_guard on public.scores;
create trigger ng_score_guard before insert or update on public.scores for each row execute function public.ng_score_guard();

alter table public.saves drop constraint if exists saves_size;
alter table public.saves add constraint saves_size check (length(data::text) < 300000);

-- 11-01 23:40 排行榜加死亡次数
alter table public.scores add column if not exists deaths int not null default 0;
